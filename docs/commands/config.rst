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

       {'allow_library_path_paste': False,
        'allow_user_creation': True,
        'allow_user_dataset_purge': True,
        'allow_user_deletion': False,
        'enable_unique_workflow_defaults': False,
        'ftp_upload_dir': '/SOMEWHERE/galaxy/ftp_dir',
        'ftp_upload_site': 'galaxy.com',
        'library_import_dir': 'None',
        'logo_url': None,
        'support_url': 'https://galaxyproject.org/support',
        'terms_url': None,
        'user_library_import_dir': None,
        'wiki_url': 'https://galaxyproject.org/'}

**Options**::


      -h, --help  Show this message and exit.


``get_version`` command
-----------------------

**Usage**::

    parsec config get_version [OPTIONS]

**Help**

Get the current version of the Galaxy instance.


**Output**


    Version of the Galaxy instance
     For example::

       {'extra': {}, 'version_major': '17.01'}

**Options**::


      -h, --help  Show this message and exit.

