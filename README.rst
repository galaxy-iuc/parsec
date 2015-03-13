================================
Parsec: the BioBlend CLI Utility
================================

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest
		:target: https://parsec.readthedocs.org.

.. image:: https://landscape.io/github/galaxy-iuc/parsec/master/landscape.svg?stytle=flat
        :target: https://landscape.io/github/galaxy-iuc/parsec/master

.. image:: https://requires.io/github/galaxy-iuc/parsec/requirements.svg?branch=master
        :target: https://requires.io/github/galaxy-iuc/parsec/requirements/?branch=master
        :alt: Requirements Status


Command-line utilities to assist in working with a Galaxy_ server instance.

* Free software: Apache License v2
* Documentation: https://parsec.readthedocs.org.
* Code: https://github.com/galaxy-iuc/parsec

Quick Start
-----------

This quick start demonstrates using ``parsec`` commands to help
run Galaxy tools.

Connect to a Galaxy server
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a running Galaxy server, you will need an account on that Galaxy instance and an API key for the account. Instructions on getting an API key can be found at http://wiki.galaxyproject.org/Learn/API .

First initialize the parsec configuration file in ``~/.parsec.yml`` via the ``parsec`` command ``config_init``::


    user@host:~$ parsec config_init
    No parsec config file found, continuning anyway...
    Wrote configuration template to ~/.paresc.yml, please open with editor and fill out.

This will look something like the following::

    ## Parsec Global Configuration File.
    # Each stanza should contian a single galaxy server to control.
    #
    # You can set the key __default to the name of a default instance
    # __default: local

    local:
        key: "<TODO>"
        email: "<TODO>"
        password: "<TODO>"
        url: "<TODO>"
        admin: False

Once those fields are filled out (and setting ``__default`` is highly recommended), parsec will now be usable from the command line.

A quick note about using different galaxy instance, the syntax is a little different than one might expect::

    user@host:~$ parsec --galaxy_instance admin histories_get_histories

Otherwise parsec will use the default galaxy instance. An admin account is required for a few actions like creation of data libraries.

.. _view-histories-and-datasets:

View Histories and Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Methods for accessing histories and datasets are grouped under ``parsec histories_*`` and ``parsec datasets_*``, respectively.

To get information on the Histories currently in your account, call::

    user@host:~$ parsec histories_get_histories
    [
        {
            "name": "RNAseq_DGE_BASIC_Prep",
            "tags": [],
            "deleted": false,
            "purged": false,
            "id": "f3c2b0f3ecac9f02",
            "url": "/api/histories/f3c2b0f3ecac9f02",
            "published": false,
            "model_class": "History",
            "annotation": null
        }
    ]

This returns a list of dictionaries containing basic metadata, including the id
and name of each History. To get more detailed information about a History we
can pass its id to the ``parsec histories_show_history`` script::

    user@host:~$ parsec histories_show_history f3c2b0f3ecac9f02
    {
        "importable": false,
        "create_time": "2015-02-27T23:01:11.766560",
        "contents_url": "/api/histories/f3c2b0f3ecac9f02/contents",
        "size": 0,
        "user_id": "ebfb8f50c6abde6d",
        "username_and_slug": null,
        "annotation": null,
        "state_details": {
            "paused": 0,
            "ok": 0,
            "failed_metadata": 0,
            "upload": 0,
            "discarded": 0,
            "resubmitted": 0,
            "running": 0,
            "setting_metadata": 0,
            "error": 0,
            "new": 0,
            "queued": 0,
            "empty": 0
        },
        "state": "new",
        "empty": true,
        "update_time": "2015-02-27T23:01:11.766577",
        "tags": [],
        "deleted": false,
        "genome_build": null,
        'nice_size': '93.5 MB',
        "slug": null,
        'name': 'RNAseq_DGE_BASIC_Prep',
        "url": "/api/histories/f3c2b0f3ecac9f02",
        "state_ids": {
            "paused": [],
            "ok": [
                'd6842fb08a76e351',
                '10a4b652da44e82a',
                '81c601a2549966a0',
                'a154f05e3bcee26b',
                '1352fe19ddce0400',
                '06d549c52d753e53',
                '9ec54455d6279cc7'
            ],
            "failed_metadata": [],
            "upload": [],
            "discarded": [],
            "resubmitted": [],
            "running": [],
            "setting_metadata": [],
            "error": [],
            "new": [],
            "queued": [],
            "empty": []
        },
        "published": false,
        "model_class": "History",
        "purged": false
    }

.. _example-dataset:

This gives us a dictionary containing the History's metadata. With ``contents=False`` (the default), we only get a list of ids of the datasets contained within the History; with ``contents=True`` we would get metadata on each dataset. We can also directly access more detailed information on a particular dataset by passing its id to the ``show_dataset`` method::

    user@host:~$ parsec datasets_show_dataset 10a4b652da44e82a
    {
        "accessible": true,
        "annotation": null,
        "api_type": "file",
        "create_time": "2015-02-27T23:46:27.642906",
        "data_type": "galaxy.datatypes.data.Text",
        "dataset_id": "10a4b652da44e82a",
        "deleted": false,
        "display_apps": [],
        "display_types": [],
        "download_url": "/api/histories/f3c2b0f3ecac9f02/contents/10a4b652da44e82a/display",
        "extension": "fastq",
        "file_ext": "fastq",
        "file_path": null,
        "file_size": 16527060,
        "genome_build": "dm3",
        "hda_ldda": "hda",
        "hid": 1,
        "history_content_type": "dataset",
        "history_id": "f3c2b0f3ecac9f02",
        "id": "10a4b652da44e82a",
        "meta_files": [],
        "metadata_data_lines": 4,
        "metadata_dbkey": "dm3",
        "misc_blurb": "15.8 MB",
        "misc_info": "uploaded fastqsanger file",
        "model_class": "HistoryDatasetAssociation",
        "name": "C1_R2_1.chr4.fq",
        "purged": false,
        "resubmitted": false,
        "state": "ok",
        "tags": [],
        "type": "file",
        "update_time": "2015-02-27T23:46:34.659590",
        "url": "/api/histories/f3c2b0f3ecac9f02/contents/10a4b652da44e82a",
        "uuid": "ccad6f3a-f75d-472f-9142-2d4c39ad1a35",
        "visible": true,
        "visualizations": []
    }

View Data Libraries
~~~~~~~~~~~~~~~~~~~

Methods for accessing Data Libraries are grouped under ``GalaxyInstance.libraries.*``. Most Data Library methods are available to all users, but as only administrators can create new Data Libraries within Galaxy, the ``create_folder`` and ``create_library`` methods can only be called using an API key belonging to an admin account.

We can view the Data Libraries available to our account using::

    user@host:~$ parsec libraries_get_libraries
    [
        {
            "can_user_add": false, 
            "description": "RNA-Seq workshop data", 
            "deleted": false, 
            "can_user_manage": false, 
            "can_user_modify": false, 
            "public": true, 
            "synopsis": "Data for the RNA-Seq tutorial", 
            "root_folder_id": "Ff2db41e1fa331b3e", 
            "model_class": "Library", 
            "id": "f2db41e1fa331b3e", 
            "name": "RNA-seq workshop data"
        }
    ]

This gives a list of metadata dictionaries with basic information on each library. We can get more information on a particular Data Library by passing its id to the ``show_library`` method::

    user@host:~$ parsec libraries_get_libraries
    {
        "can_user_add": false, 
        "description": "RNA-Seq workshop data", 
        "deleted": false, 
        "can_user_manage": false, 
        "can_user_modify": false, 
        "public": true, 
        "synopsis": "Data for the RNA-Seq tutorial", 
        "root_folder_id": "Ff2db41e1fa331b3e", 
        "model_class": "Library", 
        "id": "f2db41e1fa331b3e", 
        "name": "RNA-seq workshop data"
    }


View Workflows
~~~~~~~~~~~~~~

Methods for accessing workflows are grouped under ``GalaxyInstance.workflows.*``.

To get information on the Workflows currently in your account, use::

    user@host:~$ parsec workflows_get_workflows
    [
        {
            'id': 'e8b85ad72aefca86',
            'name': u"TopHat + cufflinks part 1",
            'url': '/api/workflows/e8b85ad72aefca86'
        },
        {
           'id': 'b0631c44aa74526d',
            'name': 'CuffDiff',
            'url': '/api/workflows/b0631c44aa74526d'
        }
    ]

This returns a list of metadata dictionaries. We can get the details of a particular Workflow, including its steps, by passing its id to the ``show_workflow`` method::

    user@host:~$ parsec workflows_show_workflow e8b85ad72aefca86
    {'id': 'e8b85ad72aefca86',
     'inputs':
        {'252':
           {'label': 'Input RNA-seq fastq',
            'value': ''
            }
         },
     'name': u"TopHat + cufflinks part 1",
     'steps':
        {'250':
           {'id': 250,
            'input_steps':
               {'input1':
                  {'source_step': 252,
                   'step_output': 'output'
                   }
               },
            'tool_id': 'tophat',
            'type': 'tool'
            },
         '251':
            {'id': 251,
             'input_steps':
                {'input':
                   {'source_step': 250,
                    'step_output': 'accepted_hits'
                    }
                },
             'tool_id': 'cufflinks',
             'type': 'tool'
             },
         '252':
            {'id': 252,
             'input_steps': {},
             'tool_id': None,
             'type': 'data_input'
             }
         },
     'url': '/api/workflows/e8b85ad72aefca86'
     }


View Users
~~~~~~~~~~

Methods for managing users are grouped under ``GalaxyInstance.users.*``. User management is only available to Galaxy administrators, that is, the API key used to connect to Galaxy must be that of an admin account.

To get a list of users, call::

    user@host:~$ parsec users_get_users 
    [
        {
            "username": "test", 
            "model_class": "User", 
            "email": "test@local.host",
            "id": "f2db41e1fa331b3e"
        },
        ...
    ]



.. _Galaxy: (http://galaxyproject.org/)
.. _GitHub: https://github.com/
