from __future__ import absolute_import
import os
from bioblend import galaxy, toolshed
from .config import read_global_config, global_config_path


def get_instance(instance_name=None):
    conf = read_global_config()
    if len(conf.keys()) == 0:
        # Probably creating the file for the first time.
        raise Exception("No galaxy instances defined")

    if instance_name is None or instance_name == '__default':
        try:
            instance_name = conf['__default']
        except KeyError:
            raise Exception("Unknown Galaxy instance and no __default provided")

    if instance_name not in conf:
        raise Exception("Unknown Galaxy instance; check spelling or add to %s" % global_config_path())

    return conf[instance_name]


def get_galaxy_instance(instance_name=None):
    conf = get_instance(instance_name=instance_name)
    return galaxy.GalaxyInstance(conf['url'],
                                 conf['key'])


def get_toolshed_instance(instance_name=None):
    conf = get_instance(instance_name=instance_name)
    return toolshed.ToolShedInstance(conf['url'],
                                     conf['key'])
