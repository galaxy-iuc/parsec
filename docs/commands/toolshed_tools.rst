toolshed_tools
==============

This section is auto-generated from the help text for the parsec command
``toolshed_tools``.


``search_tools`` command
------------------------

**Usage**::

    parsec toolshed_tools search_tools [OPTIONS] Q

**Help**

Search for tools in a Galaxy Tool Shed.


**Output**


    dictionary containing search hits as well as metadata for the
     search. For example::

       {'hits': [{'matched_terms': [],
                  'score': 3.0,
                  'tool': {'description': 'convert between various FASTQ quality formats',
                           'id': '69819b84d55f521efda001e0926e7233',
                           'name': 'FASTQ Groomer',
                           'repo_name': None,
                           'repo_owner_username': 'devteam'}},
                 {'matched_terms': [],
                  'score': 3.0,
                  'tool': {'description': 'converts a bam file to fastq files.',
                           'id': '521e282770fd94537daff87adad2551b',
                           'name': 'Defuse BamFastq',
                           'repo_name': None,
                           'repo_owner_username': 'jjohnson'}}],
        'hostname': 'https://testtoolshed.g2.bx.psu.edu/',
        'page': '1',
        'page_size': '2',
        'total_results': '118'}
    
**Options**::


      --page INTEGER       page requested  [default: 1]
      --page_size INTEGER  page size requested  [default: 10]
      -h, --help           Show this message and exit.
    
