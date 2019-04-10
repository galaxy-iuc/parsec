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

       {u'hits': [{u'matched_terms': [],
          u'score': 3.0,
          u'tool': {u'description': u'convert between various FASTQ quality formats',
           u'id': u'69819b84d55f521efda001e0926e7233',
           u'name': u'FASTQ Groomer',
           u'repo_name': None,
           u'repo_owner_username': u'devteam'}},
         {u'matched_terms': [],
          u'score': 3.0,
          u'tool': {u'description': u'converts a bam file to fastq files.',
           u'id': u'521e282770fd94537daff87adad2551b',
           u'name': u'Defuse BamFastq',
           u'repo_name': None,
           u'repo_owner_username': u'jjohnson'}}],
        u'hostname': u'https://testtoolshed.g2.bx.psu.edu/',
        u'page': u'1',
        u'page_size': u'2',
        u'total_results': u'118'}
    
**Options**::


      --page INTEGER       page requested  [default: 1]
      --page_size INTEGER  page size requested  [default: 10]
      -h, --help           Show this message and exit.
    
