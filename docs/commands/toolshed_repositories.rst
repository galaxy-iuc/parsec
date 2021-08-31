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

       [{'category_ids': ['c1df3132f6334b0e', 'f6d7b0037d901d9b'],
         'deleted': False,
         'deprecated': False,
         'description': 'Order Contigs',
         'homepage_url': '',
         'id': '287bd69f724b99ce',
         'name': 'best_tool_ever',
         'owner': 'billybob',
         'private': False,
         'remote_repository_url': '',
         'times_downloaded': 0,
         'type': 'unrestricted',
         'url': '/api/repositories/287bd69f724b99ce',
         'user_id': '5cefd48bc04af6d4'}]

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

       [{'deleted': False,
         'deprecated': False,
         'description': 'Galaxy Freebayes Bayesian genetic variant detector tool',
         'homepage_url': '',
         'id': '491b7a3fddf9366f',
         'long_description': 'Galaxy Freebayes Bayesian genetic variant detector tool originally included in the Galaxy code distribution but migrated to the tool shed.',
         'name': 'freebayes',
         'owner': 'devteam',
         'private': False,
         'remote_repository_url': '',
         'times_downloaded': 269,
         'type': 'unrestricted',
         'url': '/api/repositories/491b7a3fddf9366f',
         'user_id': '1de29d50c3c44272'},
        {'changeset_revision': 'd291dc763c4c',
         'do_not_test': False,
         'downloadable': True,
         'has_repository_dependencies': False,
         'id': '504be8aaa652c154',
         'includes_datatypes': False,
         'includes_tool_dependencies': True,
         'includes_tools': True,
         'includes_tools_for_display_in_tool_panel': True,
         'includes_workflows': False,
         'malicious': False,
         'repository_id': '491b7a3fddf9366f',
         'url': '/api/repository_revisions/504be8aaa652c154'},
        {'freebayes': ['Galaxy Freebayes Bayesian genetic variant detector tool',
                       'http://testtoolshed.g2.bx.psu.edu/repos/devteam/freebayes',
                       'd291dc763c4c',
                       '9',
                       'devteam',
                       {},
                       {'freebayes/0.9.6_9608597d12e127c847ae03aa03440ab63992fedf': {'changeset_revision': 'd291dc763c4c',
                                                                                     'name': 'freebayes',
                                                                                     'repository_name': 'freebayes',
                                                                                     'repository_owner': 'devteam',
                                                                                     'type': 'package',
                                                                                     'version': '0.9.6_9608597d12e127c847ae03aa03440ab63992fedf'},
                        'samtools/0.1.18': {'changeset_revision': 'd291dc763c4c',
                                            'name': 'samtools',
                                            'repository_name': 'freebayes',
                                            'repository_owner': 'devteam',
                                            'type': 'package',
                                            'version': '0.1.18'}}]}]
    
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

       [{'changeset_revision': '6e26c5a48e9a',
         'do_not_test': False,
         'downloadable': True,
         'has_repository_dependencies': False,
         'id': '92250afff777a169',
         'includes_datatypes': False,
         'includes_tool_dependencies': False,
         'includes_tools': True,
         'includes_tools_for_display_in_tool_panel': True,
         'includes_workflows': False,
         'malicious': False,
         'missing_test_components': False,
         'repository_id': '78f2604ff5e65707',
         'test_install_error': False,
         'time_last_tested': None,
         'tools_functionally_correct': False,
         'url': '/api/repository_revisions/92250afff777a169'},
        {'changeset_revision': '15a54fa11ad7',
         'do_not_test': False,
         'downloadable': True,
         'has_repository_dependencies': False,
         'id': 'd3823c748ae2205d',
         'includes_datatypes': False,
         'includes_tool_dependencies': False,
         'includes_tools': True,
         'includes_tools_for_display_in_tool_panel': True,
         'includes_workflows': False,
         'malicious': False,
         'missing_test_components': False,
         'repository_id': 'f9662009da7bfce0',
         'test_install_error': False,
         'time_last_tested': None,
         'tools_functionally_correct': False,
         'url': '/api/repository_revisions/d3823c748ae2205d'}]
    
**Options**::


      --downloadable                Can the tool be downloaded
      --malicious
      --tools_functionally_correct
      --missing_test_components
      --do_not_test
      --includes_tools
      --test_install_error
      --skip_tool_test
      -h, --help                    Show this message and exit.
    

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

       {'hits': [{'matched_terms': [],
                  'repository': {'approved': 'no',
                                 'description': 'Convert export file to fastq',
                                 'full_last_updated': '2015-01-18 09:48 AM',
                                 'homepage_url': '',
                                 'id': 'bdfa208f0cf6504e',
                                 'last_updated': 'less than a year',
                                 'long_description': 'This is a simple too to convert Solexas Export files to FASTQ files.',
                                 'name': 'export_to_fastq',
                                 'remote_repository_url': '',
                                 'repo_owner_username': 'louise',
                                 'times_downloaded': 164},
                  'score': 4.92},
                 {'matched_terms': [],
                  'repository': {'approved': 'no',
                                 'description': 'Convert BAM file to fastq',
                                 'full_last_updated': '2015-04-07 11:57 AM',
                                 'homepage_url': '',
                                 'id': '175812cd7caaf439',
                                 'last_updated': 'less than a month',
                                 'long_description': 'Use Picards SamToFastq to convert a BAM file to fastq. Useful for storing reads as BAM in Galaxy and converting to fastq when needed for analysis.',
                                 'name': 'bam_to_fastq',
                                 'remote_repository_url': '',
                                 'repo_owner_username': 'brad-chapman',
                                 'times_downloaded': 138},
                  'score': 4.14}],
        'hostname': 'https://testtoolshed.g2.bx.psu.edu/',
        'page': '1',
        'page_size': '2',
        'total_results': '64'}
    
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

       {'category_ids': ['c1df3132f6334b0e', 'f6d7b0037d901d9b'],
        'deleted': False,
        'deprecated': False,
        'description': 'Order Contigs',
        'homepage_url': '',
        'id': '287bd69f724b99ce',
        'long_description': '',
        'name': 'best_tool_ever',
        'owner': 'billybob',
        'private': False,
        'remote_repository_url': '',
        'times_downloaded': 0,
        'type': 'unrestricted',
        'url': '/api/repositories/287bd69f724b99ce',
        'user_id': '5cefd48bc04af6d4'}

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

       {'changeset_revision': '7602de1e7f32',
        'do_not_test': False,
        'downloadable': True,
        'has_repository_dependencies': False,
        'id': '504be8aaa652c154',
        'includes_datatypes': False,
        'includes_tool_dependencies': False,
        'includes_tools': True,
        'includes_tools_for_display_in_tool_panel': True,
        'includes_workflows': False,
        'malicious': False,
        'missing_test_components': True,
        'repository_id': '491b7a3fddf9366f',
        'test_install_error': False,
        'time_last_tested': None,
        'tool_test_results': {'missing_test_components': []},
        'tools_functionally_correct': False,
        'url': '/api/repository_revisions/504be8aaa652c154'}
    
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

       {'content_alert': '',
        'message': ''}

   .. versionadded:: 0.5.2
    
**Options**::


      --commit_message TEXT  Commit message used for the underlying Mercurial
                             repository backing Tool Shed repository.
    
      -h, --help             Show this message and exit.
    
