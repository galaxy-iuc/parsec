#!/usr/bin/env python

import importlib
import inspect
import os
import re
import glob
import argparse


import bioblend.galaxy as bg
IGNORE_LIST = [
    'histories.download_dataset',
    'histories.get_current_history',
    'make_delete_request',
    'make_get_request',
    'make_post_request',
    'make_put_request',
]



PARAM_TRANSLATION = {
    'str': 'str',
    'dict': 'dict',
    'int': 'int',
    'float': 'float',
    'bool': 'bool',
    'list': 'list', #TODO
    'file': 'click.File(\'rb+\')',
}

class ScriptBuilder(object):

    def __init__(self):
        self.path = os.path.realpath(__file__)
        templates = glob.glob(os.path.join(os.path.dirname(self.path), 'templates', '*'))
        self.templates = {}
        for template in templates:
            (tpl_id, ext) = os.path.splitext(os.path.basename(template))
            self.templates[tpl_id] = open(template, 'r').read()

        # TODO: refactor
        self.obj_init = 'gi = bg.GalaxyInstance("http://localhost:8080", "API_KEY")'
        self.obj_id = 'gi'
        self.obj = bg.GalaxyInstance("http://localhost:8080", "API_KEY")

    def template(self, template, opts):
        try:
            return self.templates[template] % opts
        except:
            raise Exception("Template not found")

    @classmethod
    def __click_option(cls, name='arg', helpstr='TODO', ptype=None):
        args = [
            '"--%s"' % name,
            'help="%s"' % helpstr
        ]
        if ptype is not None:
            args.append('type=%s' % ptype)
        return '@click.option(%s)\n' % ('\n'.join(['    ' + x for x in args]))

    @classmethod
    def __click_argument(cls, name='arg', ptype=None):
        args = [
            '"%s"' % name,
        ]
        if ptype is not None:
            args.append('type=%s' % ptype)
        return '@click.argument(%s)\n' % (', '.join(args), )

    @classmethod
    def load_module(cls, module_path):
        name = '.'.join(module_path)
        return importlib.import_module(name)

    def boring(self, method_name):
        if method_name.startswith('_'):
            return True
        if method_name.startswith('set_') or method_name.startswith('get_'):
            return True
        # TODO replace with check for height in hierachy
        return False

    def is_galaxyinstance(self, obj):
        return str(type(obj)) == "<class 'bioblend.galaxy.GalaxyInstance'>"

    def is_function(self, obj):
        return str(type(obj)) == "<type 'instancemethod'>"

    def is_class(self, obj):
        return str(type(obj)).startswith('<class ')

    def recursive_attr_get(self, obj, section):
        if len(section) == 0:
            return obj
        elif len(section) == 1:
            return getattr(obj, section[0])
        else:
            return getattr(self.recursive_attr_get(obj, section[0:-1]), section[-1])

    @classmethod
    def important_doc(cls, docstring):
        good = []
        if docstring is not None and len(docstring) > 0:
            for line in docstring.split('\n')[1:]:
                if line.strip() == '':
                    return ' '.join(good)
                else:
                    good.append(line.strip())
            return ' '.join(good)
        else:
            return "Warning: Undocumented Method"

    def identify_functions(self, module, path=None):
        targets = []
        if path is None:
            path = []

        current_module = self.recursive_attr_get(module, path)

        # Filter out boring
        current_module_attr = [x for x in dir(current_module) if not
                               self.boring(x) and not
                               self.is_galaxyinstance(self.recursive_attr_get(current_module,[x]))
                               and not '.'.join(path + [x]) in IGNORE_LIST
                               ]
        # Filter out functions/classes
        current_module_classes =   [x for x in current_module_attr if self.is_class(self.recursive_attr_get(current_module, [x]))]
        current_module_functions = [x for x in current_module_attr if self.is_function(self.recursive_attr_get(current_module, [x]))]

        # Add all functions as-is
        targets += [path + [x] for x in current_module_functions if not self.boring(x)]
        # Recursively add functions
        targets += [self.identify_functions(module, path=[clsname]) for clsname in current_module_classes]
        return targets

    def flatten(self, x):
        # http://stackoverflow.com/a/577971
        result = []
        for el in x:
            if isinstance(el, list):
                if isinstance(el[0], str):
                    result.append(el)
                else:
                    result.extend(self.flatten(el))
            else:
                result.append(el)
        return result

    @classmethod
    def parameter_translation(cls, k):
        try:
            return PARAM_TRANSLATION[k]
        except:
            raise Exception("Unknown parameter type " + k)

    def orig(self):

        targets = self.flatten(self.identify_functions(self.obj))

        for target in targets:
            func = self.recursive_attr_get(self.obj, target)
            candidate = '.'.join(target)

            argspec = inspect.getargspec(func)
            argdoc = func.__doc__

            data = {
                'command_name': candidate,
                'click_arguments': "",
                'click_options': "",
                'args_with_defaults': "galaxy_instance",
                'wrapped_method_args': "",
            }
            param_docs = {}
            if argdoc is not None:
                sections = [x for x in argdoc.split("\n\n")]
                sections = [re.sub('\s+', ' ', x.strip()) for x in sections if x != '']
                paramre = re.compile(":type (?P<param_name>[^:]+): (?P<param_type>[^:]+) :param (?P<param_name2>[^:]+): (?P<desc>.+)")
                for subsec in sections:
                    m = paramre.match(subsec)
                    if m:
                        assert m.group('param_name') == m.group('param_name2')
                        param_docs[m.group('param_name')] = {'type': m.group('param_type'),
                                                             'desc': m.group('desc')}


            # Ignore with only cls/self
            if len(argspec.args) > 1:
                method_signature = ['galaxy_instance']
                # Args and kwargs are separate, as args should come before kwargs
                method_signature_args = []
                method_signature_kwargs = []
                method_exec_args = []
                method_exec_kwargs = []

                for i, k in enumerate(argspec.args[1:]):
                    # Sometimes deafults = None when it should = (None)
                    # So we hack around this
                    try:
                        v = argspec.defaults[i-1]
                    except Exception, e:
                        v = None

                    try:
                        param_type = self.parameter_translation(param_docs[k]['type'])
                    except Exception, e:
                        param_type = None
                        print candidate, e

                    # If v is not None, then it's a kwargs, otherwise an arg
                    if v is not None:
                        # Strings must be treated specially by removing their value
                        if isinstance(v, str):
                            v = '""'
                        # All other instances of V are fine, e.g. boolean=False or int=1000

                        # Register twice as the method invocation uses v=k
                        method_signature_kwargs.append("%s=%s" % (k, v))
                        method_exec_kwargs.append('%s=%s' % (k, k))

                        # TODO: refactor
                        try:
                            descstr = param_docs[k]['desc']
                        except KeyError:
                            print "Error finding %s in %s" % (k, candidate)
                            print ""
                            descstr = None
                        data['click_options'] += self.__click_option(name=k, helpstr=descstr, ptype=param_type)
                    else:
                        # Args, not kwargs
                        method_signature_args.append(k)
                        method_exec_args.append(k)
                        data['click_arguments'] += self.__click_argument(name=k, ptype=param_type)



                # Complete args
                data['args_with_defaults'] = ', '.join(method_signature +
                                                    method_signature_args +
                                                    method_signature_kwargs)
                data['wrapped_method_args'] = ', '.join(method_exec_args +
                                                        method_exec_kwargs)

            # My function is more effective until can figure out docstring
            data['short_docstring'] = self.important_doc(argdoc)
            # Full method call
            data['wrapped_method'] = 'gi.' + candidate

            # Generate a command name, prefix everything with auto_ to identify the
            # automatically generated stuff
            cmd_name = 'cmd_%s.py' % candidate
            cmd_path = os.path.join('parsec', 'commands', cmd_name)

            # Save file
            with open(cmd_path, 'w') as handle:
                handle.write(self.template('click', data))

if __name__ == '__main__':
    z = ScriptBuilder()
    z.orig()
