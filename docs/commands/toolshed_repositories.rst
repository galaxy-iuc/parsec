toolshed_repositories
=====================

This section is auto-generated from the help text for the parsec command
``toolshed_repositories``.


``create_repository`` command
-----------------------------

**Usage**::

    parsec toolshed_repositories create_repository [OPTIONS] NAME SYNOPSIS

**Help**

Create a new repository in a Tool Shed.


**Output**


    a dictionary containing information about the new repository.
     For example::

       {"deleted": false,
        "deprecated": false,
        "description": "new_synopsis",
        "homepage_url": "https://github.com/galaxyproject/",
        "id": "8cf91205f2f737f4",
        "long_description": "this is some repository",
        "model_class": "Repository",
        "name": "new_repo_17",
        "owner": "qqqqqq",
        "private": false,
        "remote_repository_url": "https://github.com/galaxyproject/tools-devteam",
        "times_downloaded": 0,
        "type": "unrestricted",
        "user_id": "adb5f5c93f827949"}
    
**Options**::


      --description TEXT            Optional description of the repository
      --type TEXT                   type of the repository. One of "unrestricted",
                                    "repository_suite_definition", or
                                    "tool_dependency_definition"  [default:
                                    unrestricted]
      --remote_repository_url TEXT  Remote URL (e.g. GitHub/Bitbucket repository)
      --homepage_url TEXT           Upstream's homepage for the project
      --category_ids TEXT           List of encoded category IDs
      -h, --help                    Show this message and exit.
    

``get_ordered_installable_revisions`` command
---------------------------------------------

**Usage**::

    parsec toolshed_repositories get_ordered_installable_revisions 

**Help**

Returns the ordered list of changeset revision hash strings that are associated with installable revisions. As in the changelog, the list is ordered oldest to newest.


**Output**


    List of changeset revision hash strings from oldest to newest
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_repositories`` command
----------------------------

**Usage**::

    parsec toolshed_repositories get_repositories [OPTIONS]

**Help**

Get a list of all the repositories in a Galaxy Tool Shed.


**Output**


    Returns a list of dictionaries containing information about
     repositories present in the Tool Shed.
     For example::

       [{u'category_ids': [u'c1df3132f6334b0e', u'f6d7b0037d901d9b'],
         u'deleted': False,
         u'deprecated': False,
         u'description': u'Order Contigs',
         u'homepage_url': u'',
         u'id': u'287bd69f724b99ce',
         u'name': u'best_tool_ever',
         u'owner': u'billybob',
         u'private': False,
         u'remote_repository_url': u'',
         u'times_downloaded': 0,
         u'type': u'unrestricted',
         u'url': u'/api/repositories/287bd69f724b99ce',
         u'user_id': u'5cefd48bc04af6d4'}]

   .. versionchanged:: 0.4.1
     Changed method name from ``get_tools`` to ``get_repositories`` to
     better align with the Tool Shed concepts.
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_repository_revision_install_info`` command
------------------------------------------------

**Usage**::

    parsec toolshed_repositories get_repository_revision_install_info 

**Help**

Return a list of dictionaries of metadata about a certain changeset revision for a single tool.


**Output**


    Returns a list of the following dictionaries:

     #. a dictionary defining the repository
     #. a dictionary defining the repository revision (RepositoryMetadata)
     #. a dictionary including the additional information required to
        install the repository

     For example::

                [{u'deleted': False,
                  u'deprecated': False,
                  u'description': u'Galaxy Freebayes Bayesian genetic variant detector tool',
                  u'homepage_url': u'',
                  u'id': u'491b7a3fddf9366f',
                  u'long_description': u'Galaxy Freebayes Bayesian genetic variant detector tool originally included in the Galaxy code distribution but migrated to the tool shed.',
                  u'name': u'freebayes',
                  u'owner': u'devteam',
                  u'private': False,
                  u'remote_repository_url': u'',
                  u'times_downloaded': 269,
                  u'type': u'unrestricted',
                  u'url': u'/api/repositories/491b7a3fddf9366f',
                  u'user_id': u'1de29d50c3c44272'},
                 {u'changeset_revision': u'd291dc763c4c',
                  u'do_not_test': False,
                  u'downloadable': True,
                  u'has_repository_dependencies': False,
                  u'id': u'504be8aaa652c154',
                  u'includes_datatypes': False,
                  u'includes_tool_dependencies': True,
                  u'includes_tools': True,
                  u'includes_tools_for_display_in_tool_panel': True,
                  u'includes_workflows': False,
                  u'malicious': False,
                  u'repository_id': u'491b7a3fddf9366f',
                  u'url': u'/api/repository_revisions/504be8aaa652c154'},
                 {u'freebayes': [u'Galaxy Freebayes Bayesian genetic variant detector tool',
                   u'http://testtoolshed.g2.bx.psu.edu/repos/devteam/freebayes',
                   u'd291dc763c4c',
                   u'9',
                   u'devteam',
                   {},
                   {u'freebayes/0.9.6_9608597d12e127c847ae03aa03440ab63992fedf': {u'changeset_revision': u'd291dc763c4c',
                     u'name': u'freebayes',
                     u'repository_name': u'freebayes',
                     u'repository_owner': u'devteam',
                     u'type': u'package',
                     u'version': u'0.9.6_9608597d12e127c847ae03aa03440ab63992fedf'},
                    u'samtools/0.1.18': {u'changeset_revision': u'd291dc763c4c',
                     u'name': u'samtools',
                     u'repository_name': u'freebayes',
                     u'repository_owner': u'devteam',
                     u'type': u'package',
                     u'version': u'0.1.18'}}]}]
    
**Options**::


      -h, --help  Show this message and exit.
    

``repository_revisions`` command
--------------------------------

**Usage**::

    parsec toolshed_repositories repository_revisions [OPTIONS]

**Help**

Returns a (possibly filtered) list of dictionaries that include information about all repository revisions. The following parameters can be used to filter the list.


**Output**


    Returns a (possibly filtered) list of dictionaries that include
     information about all repository revisions.
     For example::

       [{u'changeset_revision': u'6e26c5a48e9a',
         u'do_not_test': False,
         u'downloadable': True,
         u'has_repository_dependencies': False,
         u'id': u'92250afff777a169',
         u'includes_datatypes': False,
         u'includes_tool_dependencies': False,
         u'includes_tools': True,
         u'includes_tools_for_display_in_tool_panel': True,
         u'includes_workflows': False,
         u'malicious': False,
         u'missing_test_components': False,
         u'repository_id': u'78f2604ff5e65707',
         u'test_install_error': False,
         u'time_last_tested': None,
         u'tools_functionally_correct': False,
         u'url': u'/api/repository_revisions/92250afff777a169'},
        {u'changeset_revision': u'15a54fa11ad7',
         u'do_not_test': False,
         u'downloadable': True,
         u'has_repository_dependencies': False,
         u'id': u'd3823c748ae2205d',
         u'includes_datatypes': False,
         u'includes_tool_dependencies': False,
         u'includes_tools': True,
         u'includes_tools_for_display_in_tool_panel': True,
         u'includes_workflows': False,
         u'malicious': False,
         u'missing_test_components': False,
         u'repository_id': u'f9662009da7bfce0',
         u'test_install_error': False,
         u'time_last_tested': None,
         u'tools_functionally_correct': False,
         u'url': u'/api/repository_revisions/d3823c748ae2205d'}]
    
**Options**::


      --downloadable                  Can the tool be downloaded
      --malicious TEXT
      --tools_functionally_correct TEXT
      --missing_test_components TEXT
      --do_not_test TEXT
      --includes_tools TEXT
      --test_install_error TEXT
      --skip_tool_test TEXT
      -h, --help                      Show this message and exit.
    

``search_repositories`` command
-------------------------------

**Usage**::

    parsec toolshed_repositories search_repositories [OPTIONS] Q

**Help**

Search for repositories in a Galaxy Tool Shed.


**Output**


    dictionary containing search hits as well as metadata for the
     search.
     For example::

       {u'hits': [{u'matched_terms': [],
          u'repository': {u'approved': u'no',
           u'description': u'Convert export file to fastq',
           u'full_last_updated': u'2015-01-18 09:48 AM',
           u'homepage_url': u'',
           u'id': u'bdfa208f0cf6504e',
           u'last_updated': u'less than a year',
           u'long_description': u'This is a simple too to convert Solexas Export files to FASTQ files.',
           u'name': u'export_to_fastq',
           u'remote_repository_url': u'',
           u'repo_owner_username': u'louise',
           u'times_downloaded': 164},
          u'score': 4.92},
         {u'matched_terms': [],
          u'repository': {u'approved': u'no',
           u'description': u'Convert BAM file to fastq',
           u'full_last_updated': u'2015-04-07 11:57 AM',
           u'homepage_url': u'',
           u'id': u'175812cd7caaf439',
           u'last_updated': u'less than a month',
           u'long_description': u'Use Picards SamToFastq to convert a BAM file to fastq. Useful for storing reads as BAM in Galaxy and converting to fastq when needed for analysis.',
           u'name': u'bam_to_fastq',
           u'remote_repository_url': u'',
           u'repo_owner_username': u'brad-chapman',
           u'times_downloaded': 138},
          u'score': 4.14}],
        u'hostname': u'https://testtoolshed.g2.bx.psu.edu/',
        u'page': u'1',
        u'page_size': u'2',
        u'total_results': u'64'}
    
**Options**::


      --page INTEGER       page requested  [default: 1]
      --page_size INTEGER  page size requested  [default: 10]
      -h, --help           Show this message and exit.
    

``show_repository`` command
---------------------------

**Usage**::

    parsec toolshed_repositories show_repository [OPTIONS] TOOLSHED_ID

**Help**

Display information of a repository from Tool Shed


**Output**


    Information about the tool.
     For example::

       {u'category_ids': [u'c1df3132f6334b0e', u'f6d7b0037d901d9b'],
        u'deleted': False,
        u'deprecated': False,
        u'description': u'Order Contigs',
        u'homepage_url': u'',
        u'id': u'287bd69f724b99ce',
        u'long_description': u'',
        u'name': u'best_tool_ever',
        u'owner': u'billybob',
        u'private': False,
        u'remote_repository_url': u'',
        u'times_downloaded': 0,
        u'type': u'unrestricted',
        u'url': u'/api/repositories/287bd69f724b99ce',
        u'user_id': u'5cefd48bc04af6d4'}

   .. versionchanged:: 0.4.1
     Changed method name from ``show_tool`` to ``show_repository`` to
     better align with the Tool Shed concepts.
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_repository_revision`` command
------------------------------------

**Usage**::

    parsec toolshed_repositories show_repository_revision 

**Help**

Returns a dictionary that includes information about a specified repository revision.


**Output**


    Returns a dictionary that includes information about a
     specified repository revision.
     For example::

       {u'changeset_revision': u'7602de1e7f32',
        u'do_not_test': False,
        u'downloadable': True,
        u'has_repository_dependencies': False,
        u'id': u'504be8aaa652c154',
        u'includes_datatypes': False,
        u'includes_tool_dependencies': False,
        u'includes_tools': True,
        u'includes_tools_for_display_in_tool_panel': True,
        u'includes_workflows': False,
        u'malicious': False,
        u'missing_test_components': True,
        u'repository_id': u'491b7a3fddf9366f',
        u'test_install_error': False,
        u'time_last_tested': None,
        u'tool_test_results': {u'missing_test_components': []},
        u'tools_functionally_correct': False,
        u'url': u'/api/repository_revisions/504be8aaa652c154'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_repository`` command
-----------------------------

**Usage**::

    parsec toolshed_repositories update_repository [OPTIONS] ID TAR_BALL_PATH

**Help**

Update the contents of a Tool Shed repository with specified tar ball.


**Output**


    Returns a dictionary that includes repository content warnings.
     Most valid uploads will result in no such warning and an exception
     will be raised generally if there are problems.
     For example a successful upload will look like::

       {u'content_alert': u'',
        u'message': u''}

   .. versionadded:: 0.5.2
    
**Options**::


      --commit_message TEXT  Commit message used for the underlying Mercurial
                             repository backing Tool Shed repository.
      -h, --help             Show this message and exit.
    
