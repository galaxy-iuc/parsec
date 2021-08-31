tool_dependencies
=================

This section is auto-generated from the help text for the parsec command
``tool_dependencies``.


``summarize_toolbox`` command
-----------------------------

**Usage**::

    parsec tool_dependencies summarize_toolbox [OPTIONS]

**Help**

Summarize requirements across toolbox (for Tool Management grid).


**Output**


    dictified descriptions of the dependencies, with attribute
     `dependency_type: None` if no match was found.
     For example::

       [{'requirements': [{'name': 'galaxy_sequence_utils',
                           'specs': [],
                           'type': 'package',
                           'version': '1.1.4'},
                          {'name': 'bx-python',
                           'specs': [],
                           'type': 'package',
                           'version': '0.8.6'}],
         'status': [{'cacheable': False,
                     'dependency_type': None,
                     'exact': True,
                     'model_class': 'NullDependency',
                     'name': 'galaxy_sequence_utils',
                     'version': '1.1.4'},
                     {'cacheable': False,
                     'dependency_type': None,
                     'exact': True,
                     'model_class': 'NullDependency',
                     'name': 'bx-python',
                     'version': '0.8.6'}],
         'tool_ids': ['vcf_to_maf_customtrack1']}]

   .. note::
     This method can only be used with Galaxy ``release_20.01`` or later and requires
       the user to be an admin. It relies on an experimental API particularly tied to
       the GUI and therefore is subject to breaking changes.
    
**Options**::


      --index INTEGER        index of the dependency resolver with respect to the
                             dependency resolvers config file
    
      --tool_ids TEXT        tool_ids to return when index_by=tools
      --resolver_type TEXT   restrict to specified resolver type
      --include_containers   include container resolvers in resolution
      --container_type TEXT  restrict to specified container type
      --index_by TEXT        By default results are grouped by requirements. Set to
                             'tools' to return one entry per tool.  [default:
                             requirements]
    
      -h, --help             Show this message and exit.
    
