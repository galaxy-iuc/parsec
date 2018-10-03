config
======

This section is auto-generated from the help text for the parsec command
``config``.


``get_config`` command
----------------------

**Usage**::

    parsec config get_config [OPTIONS]

**Help**

Get a list of attributes about the Galaxy instance. More attributes will be present if the user is an admin.


**Output**


    A list of attributes.
     For example::

       {u'allow_library_path_paste': False,
        u'allow_user_creation': True,
        u'allow_user_dataset_purge': True,
        u'allow_user_deletion': False,
        u'enable_unique_workflow_defaults': False,
        u'ftp_upload_dir': u'/SOMEWHERE/galaxy/ftp_dir',
        u'ftp_upload_site': u'galaxy.com',
        u'library_import_dir': u'None',
        u'logo_url': None,
        u'support_url': u'https://galaxyproject.org/support',
        u'terms_url': None,
        u'user_library_import_dir': None,
        u'wiki_url': u'https://galaxyproject.org/'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_version`` command
-----------------------

**Usage**::

    parsec config get_version [OPTIONS]

**Help**

Get the current version of the Galaxy instance. This functionality is available since Galaxy ``release_15.03``.


**Output**


    Version of the Galaxy instance

   For example::

       {'extra': {}, 'version_major': '17.01'}
    
**Options**::


      -h, --help  Show this message and exit.
    
