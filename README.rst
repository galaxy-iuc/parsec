====================================
Parsec: Galaxy at the Speed of Light
====================================

.. image:: https://img.shields.io/pypi/v/galaxy-parsec.svg
        :target: https://pypi.org/project/galaxy-parsec/
        :alt: PyPi

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest
        :target: https://parsec.readthedocs.org
        :alt: Documentation

.. image:: https://requires.io/github/galaxy-iuc/parsec/requirements.svg?branch=master
        :target: https://requires.io/github/galaxy-iuc/parsec/requirements/?branch=master
        :alt: Requirements Status

.. image:: https://travis-ci.org/galaxy-iuc/parsec.svg?branch=master
        :target: https://travis-ci.org/galaxy-iuc/parsec
        :alt: Build Status

.. image:: https://img.shields.io/github/license/galaxy-iuc/parsec.svg
        :target: https://github.com/galaxy-iuc/parsec/blob/master/LICENSE
        :alt: License



Command-line utilities to assist in working with Galaxy_ servers.

Installation
------------

.. code-block:: shell

   $ pip install galaxy-parsec
   $ parsec init

Python 3.6+ is supported

Questions?
----------

|Gitter|

.. |Gitter| image:: https://badges.gitter.im/galaxy-iuc/parsec.svg
   :target: https://gitter.im/galaxy-iuc/parsec?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

Quick Start
-----------

This quick start demonstrates using ``parsec`` commands to manipulate Galaxy
histories and datasets. You will want to install `jq <https://stedolan.github.io/jq/download/>`__
if you do not have it already.

Connect to a Galaxy server
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a running Galaxy server, you will need an account on that Galaxy
instance and an API key for the account. Instructions on getting an API key can
be found at http://wiki.galaxyproject.org/Learn/API .

First initialize parsec:

.. code-block:: shell

    $ parsec init

Once initialized, parsec will be usable from the command line. Please note that
an admin account is required for a few actions like creation of data libraries,
or access to user API keys.  Your configuration must allow access to /api without
need for a username or password. More infomration can be found at
https://galaxyproject.org/admin/config/performance/production-server/

.. _view-histories-and-datasets:

Introduction To Parsec
~~~~~~~~~~~~~~~~~~~~~~

Parsec is a set of automatically generated wrappers for BioBlend functions. I
found myself writing a large number of small / one-off scripts that invoked
simple bioblend functions. These scripts were impossible to compose and use in
a linux-friendly manner. I copied and pasted code between all of these utility scripts.

Parsec is the answer to all of these problems. It extracts all of the
individual functions I was writing as separate CLI commands that can be piped
together, run in parallel, etc.

After installation, running ``parsec`` will present you with a list of sub-commands you can execute.

.. code-block:: shell

   $ parsec
   Usage: parsec [OPTIONS] COMMAND [ARGS]...

     Command line wrappers around BioBlend functions. While this sounds
     unexciting, with parsec and jq you can easily build powerful command line
     scripts.

   Options:
     --version               Show the version and exit.
     -v, --verbose           Enables verbose mode.
     --galaxy_instance TEXT  name of galaxy instance from ~/.planemo.yml
                             [required]
     --help                  Show this message and exit.

   Commands:
     config
     datasets
     datatypes
     folders
     forms
     ...

Each of these commands has more commands under it:

.. code-block:: shell

   $ parsec histories
   Usage: parsec histories [OPTIONS] COMMAND [ARGS]...

   Options:
     --help  Show this message and exit.

   Commands:
     create_dataset_collection       Create a new dataset collection
     create_history                  Create a new history, optionally setting
                                     the...
     create_history_tag              Create history tag
     delete_dataset                  Mark corresponding dataset as deleted.
     delete_dataset_collection       Mark corresponding dataset collection as...
     delete_history                  Delete a history.
     download_dataset                Deprecated method, use...
     download_history                Download a history export archive.
     export_history                  Start a job to create an export archive
                                     for...
     ...



Viewing Histories and Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get information on the Histories currently in your account, call ``history
get_histories``, and we will pipe this to a ``jq`` command which selects the
first element from the JSON array.

.. code-block:: shell

    $ parsec histories get_histories | jq '.[0]'

Parsec will respond with information about your first history

.. code-block:: json

    {
      "name": "BuildID=Manual-2017.05.02T16:13 WF=PAP_2017_Comparative_(v1.0)_BOOTSTRAPPED Org=CCS Source=Jenkins",
      "url": "/galaxy/api/histories/548c0777ac615645",
      "annotation": null,
      "model_class": "History",
      "id": "548c0777ac615645",
      "tags": [
        "Automated",
        "Annotation",
        "BICH464"
      ],
      "purged": false,
      "published": false,
      "deleted": false
    }

This may not be all of the information you were expecting about your history.
In that case, you might want to call ``show_history`` which will show you more
details about a single history. You can either manually type ``parsec histories
show_history 548c0777ac615645``, or we can do this in batch:

.. code-block:: shell

    $ parsec histories get_histories | jq '.[0].id' | xargs -n 1 parsec histories show_history

Which pulls out the first history, select the ``id`` attribute, before passing it to ``xargs``.
If you have not used it before, ``xargs`` allows us to execute multiple
commands for some input data. Here we execute the command ``parsec histories
show_history`` for each line of input (i.e. each ID returned to us from the jq call).
``xargs -n 1`` ensures that we will only pass a single ID to a
single call of ``show_history``. If you were to use ``jq '.[].id'`` instead of
``jq '.[0].id'`` it would output the IDs for every history you own. You could
then pipe this to xargs and run ``show_history`` on all of your histories!

.. code-block:: json

   {
     "annotation": null,
     "contents_url": "/galaxy/api/histories/548c0777ac615645/contents",
     "create_time": "2017-05-02T16:18:21.285382",
     "deleted": false,
     "empty": false,
     "genome_build": null,
     "id": "548c0777ac615645",
     "importable": true,
     "model_class": "History",
     "name": "BuildID=Manual-2017.05.02T16:13 WF=PAP_2017_Comparative_(v1.0)_BOOTSTRAPPED Org=CCS Source=Jenkins",
     "published": false,
     "purged": false,
     "size": 34760258,
     "slug": "buildidmanual-20170502t1613-wfpap2017comparativev10bootstrapped-orgccs-sourcejenkins",
     "state": "ok",
     "state_details": {
       "discarded": 0,
       "empty": 0,
       "error": 0,
       "failed_metadata": 0,
       "new": 0,
       "ok": 29,
       "paused": 0,
       "queued": 0,
       "running": 0,
       "setting_metadata": 0,
       "upload": 0
     },
     "state_ids": {
       "discarded": [
         "a6cc986453fae8ba",
         "f2f9b7b017f20578",
         "70eb5af78c588bd1"
       ],
       "empty": [],
       "error": [
         "d643e34e1114cc52",
         "98ae3d35d73f82c9"
       ],
       "failed_metadata": [],
       "new": [],
       "ok": [
         "e510305efbee5f49",
         "0d595b7c2b6e9b93",
         "d04ac6f949ae266c",
         "175f283ddaeca39c",
         "b34432b8a0847c04",
         "ea7ff5323ddebcb8",
         "3e40a393efafc45c",
         "7ce5ec5d51ef85cb",
         "577e4242cdfbe1aa",
         "193d15527d13f45e",
         "4543f9456af7f0df",
         "5e1293df75b4f95b",
         "a57bae35eca5fbfe",
         "6c306b2ed4533f1f",
         "97c5f81b159505f0",
         "64d1d8e46b4554bd",
         "8e9432496d7e2b43",
         "5c8579257c579aae",
         "243ad216fbfa268e",
         "8336d9eb27b27677",
         "a1d4cc61bdba629d",
         "7f93a80890822fa9",
         "c479b351902302e2",
         "36b60fb58ad24a71",
         "041dd3cb6879f1f7",
         "36992e90715c9c77",
         "4bddfe152467e972",
         "2d9f5c0c36d89e10",
         "e53ad6f3133b2816"
       ],
       "paused": [
         "4a8143557292a233",
         "b0f8a75aa6be2c1d"
       ],
       "queued": [],
       "running": [],
       "setting_metadata": [],
       "upload": []
     },
     "tags": [
       "Automated",
       "Annotation",
       "BICH464"
     ],
     "update_time": "2017-05-02T16:49:07.941097",
     "url": "/galaxy/api/histories/548c0777ac615645",
     "user_id": "f570ade6e7840ba0",
     "username_and_slug": "u/helena-rasche/h/buildidmanual-20170502t1613-wfpap2017comparativev10bootstrapped-orgccs-sourcejenkins"
   }

So much metadata to play with and filter on! Note that many of these commands
have additional flags, for example ``parsec histories show_history --help``
will tell us that we can also pass the --contents option to retrieve a list of datasets in that history, even filtering on their visibility.

.. code-block:: shell

   $ parsec histories show_history --help
   Usage: parsec histories show_history [OPTIONS] HISTORY_ID

     Get details of a given history. By default, just get the history meta
     information.

   Options:
     --contents      When ``True``, the complete list of datasets in the given
                     history.
     --deleted TEXT  Used when contents=True, includes deleted datasets in
                     history dataset list
     --visible TEXT  Used when contents=True, includes only visible datasets in
                     history dataset list
     --details TEXT  Used when contents=True, includes dataset details. Set to
                     'all' for the most information

Thus with a simple query

.. code-block:: shell

   $ parsec histories show_history 548c0777ac615645 --contents --deleted True | jq -S '.[0]'

We see the first deleted dataset in the history.

.. code-block:: shell

   {
     "create_time": "2017-05-02T16:18:54.272050",
     "dataset_id": "93c926a0dabafde3",
     "deleted": true,
     "extension": "fasta",
     "hid": 30,
     "history_content_type": "dataset",
     "history_id": "548c0777ac615645",
     "id": "d643e34e1114cc52",
     "name": "Feature Sequence Export Unique on data 27 and data 20",
     "purged": false,
     "state": "error",
     "type": "file",
     "type_id": "dataset-d643e34e1114cc52",
     "update_time": "2017-05-02T16:47:57.807506",
     "url": "/galaxy/api/histories/548c0777ac615645/contents/d643e34e1114cc52",
     "visible": true
   }


This gives us a dictionary containing the History's metadata. With ``contents=False`` (the default), we only get a list of ids of the datasets contained within the History; with ``contents=True`` we would get metadata on each dataset. We can also directly access more detailed information on a particular dataset by passing its id to the ``show_dataset`` method:

.. code-block:: shell

    $ parsec datasets_show_dataset 10a4b652da44e82a
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



On JQ
-----

It is worth it to look at some of the things possible with JQ for a moment. The
above example may not be so exciting at first blush, but you can do incredible
things with the combination of parsec, jq, and xargs. Here are some examples to consider:

- find all histories with a public link, but not published in the
  shared-histories section, and print out their history name and the shared
  link.

  .. code-block:: shell

     $ parsec histories get_histories | \
        jq '.[].id' | \
        xargs -n 1 parsec histories show_history | \
        jq '. | select(.published == false) | select(.importable == true) | [.published, .importable, .id, .username_and_slug] | @tsv' -r

- reset the API keys for 30 users at once.

  .. code-block:: shell

     $ parsec users get_users | \
        jq '.[] | \
        select(.username | contains("janedoe")) | .id' | \
        xargs -n 1 parsec users create_user_apikey

- download all of the OK datasets in a set of histories

  .. code-block:: shell

     $ parsec histories get_histories | \
        jq '.[].id' | \ # Or other, more complex filtering?
        xargs -n 1 parsec histories show_history | \ # Get history details
        jq '.state_ids.ok[]' | \ # Find OK datasets
        xargs -n 1 parsec datasets download_dataset --file_path '.' --use_default_filename # Download

.. _example-dataset:


View Workflows
~~~~~~~~~~~~~~

Methods for accessing workflows are grouped under ``GalaxyInstance.workflows.*``.

To get information on the Workflows currently in your account, use:

.. code-block:: shell

    $ parsec workflows get_workflows
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

For example, to further investigate a workflow, we can request:

.. code-block:: shell

   $ parsec workflows show_workflow ded67e5aa1371841 | jq 'del(.steps)'

The workflow output is generally quite large as it embeds a full copy of the
workflow. In the above JQ command I have removed the ``steps`` attribute from
the output for brevity.

.. code-block:: json

   {
     "annotation": "",
     "model_class": "StoredWorkflow",
     "latest_workflow_uuid": "94c40212-c4bb-43b7-a43b-eadc1a3b2894",
     "id": "ded67e5aa1371841",
     "url": "/galaxy/api/workflows/ded67e5aa1371841",
     "deleted": false,
     "tags": [],
     "owner": "helena-rasche",
     "name": "PAP 2017 Functional (v8.15)",
     "inputs": {
       "0": {
         "value": "",
         "uuid": "9397916e-afb7-4e48-b89e-d4c99bf202de",
         "label": "Apollo Organism JSON File"
       },
       "2": {
         "value": "",
         "uuid": "eca835c6-328a-4698-a387-d0719b24d19d",
         "label": "Genome Sequence"
       },
       "1": {
         "value": "",
         "uuid": "5511d038-e96b-49b2-998a-d037935f6e06",
         "label": "Annotation Set"
       }
     },
     "published": false
   }


View Users
~~~~~~~~~~

Methods for managing users are grouped under ``GalaxyInstance.users.*``. User management is only available to Galaxy administrators, that is, the API key used to connect to Galaxy must be that of an admin account.

To get a list of users, call::

    $ parsec users get_users
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


In Depth Example
~~~~~~~~~~~~~~~~

As a more detailed example, we'll launch a simple workflow.

Step 1. What are the Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

   $ parsec workflows show_workflow ded67e5aa1371841 | jq .inputs > inputs.json

In practice this file probably looks similar to this:

.. code-block:: json

   {
     "0": {
       "value": "",
       "uuid": "9397916e-afb7-4e48-b89e-d4c99bf202de",
       "label": "Apollo Organism JSON File"
     },
     "2": {
       "value": "",
       "uuid": "eca835c6-328a-4698-a387-d0719b24d19d",
       "label": "Genome Sequence"
     },
     "1": {
       "value": "",
       "uuid": "5511d038-e96b-49b2-998a-d037935f6e06",
       "label": "Annotation Set"
     }
   }


Step 2: Prepare History and Load Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, we'll create a history to manage all of our work:

.. code-block:: shell

   $ HISTORY_ID=$(parsec histories create_history | jq .id)
   $ parsec histories update_history --name 'Parsec test'

Next we have to fetch some datasets. You could upload them:

.. code-block:: shell

   $ parsec tools upload_file my-file.gff3 $HISTORY_ID

But in my case, I need to run a tool which produces them:

.. code-block:: shell

   JOB_ID=$(parsec tools run_tool $HISTORY_ID edu.tamu.cpt2.webapollo.export \
      '{"org_source|source_select": "direct", "org_source|org_raw": "Miro"}' | \
      jq .id)

   $ parsec jobs show_job .outputs $JOB_ID

By storing the job ID in a variable, we can make repeated requests to check on
it. The second parsec statement fetches the output datasets from this step.

.. code-block:: json

   {
     "fasta_out": {
       "id": "61513e15ce98c986",
       "src": "hda",
       "uuid": "0de1442b-c410-4a38-b9ca-49cff973d9b8"
     },
     "gff_out": {
       "id": "62ee69adcf74378c",
       "src": "hda",
       "uuid": "887aaf6f-ed07-4ee8-a396-c16612f83d83"
     },
     "json_out": {
       "id": "1f73e96543934ac8",
       "src": "hda",
       "uuid": "3be3d364-83c5-4a23-87fa-ebd8c27f2094"
     }
   }


Step 3: Invoking the Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remembering back to the inputs in step 1, we will match them up and create an ``inputs.json`` file

- 0 / organism json file => json_out
- 1 / genome sequence  => gff_out
- 2 / annotation set => fasta_out

This gives us an inputs.json that looks like so:

.. code-block:: json

   {
     "0": {
       "id": "1f73e96543934ac8",
       "src": "hda"
     },
     "1": {
       "id": "62ee69adcf74378c",
       "src": "hda"
     },
     "2": {
       "id": "61513e15ce98c986",
       "src": "hda"
     }
   }

We can now invoke our workflow using parsec!
Since the inputs is a JSON parameter, it can be supplied many different ways for your convenience. All of the following behave identically.

.. code-block:: shell

   $ cat params.json | parsec jobs search_jobs -; # Stdin
   $ parsec jobs search_jobs params.json; # Filename
   $ parsec jobs search_jobs $(cat params.json); # String argument

Running the invocation:

.. code-block:: shell

   $ parsec workflows invoke_workflow ded67e5aa1371841 --inputs inputs.json --history_id $HISTORY_ID

Produces a very succinct workflow launch output:

.. code-block:: json

   {
       "uuid": "94246003-2f8b-11e7-9427-20474784cc00",
       "state": "new",
       "workflow_id": "3daf5606d767a471",
       "id": "c7f60cfda02f0f46",
       "update_time": "2017-05-02T23:03:39.693288",
       "model_class": "WorkflowInvocation",
       "history_id": "0d17c6f8cd8d49a5"
   }

We can now use parsec to check on the status of all of the datasets:

.. code-block:: shell

   $ parsec workflows show_invocation 3daf5606d767a471 c7f60cfda02f0f46 | jq '.steps[].state' | sort | uniq -c
      3 "running"
     72 "new"
      3 null
      1 "ok"

Or we can use one of the utility scripts to wait on that workflow to finish before continuing on to some other task:

.. code-block:: shell

   $ parsec utils wait_on_invocation 3daf5606d767a471 c7f60cfda02f0f46 && ...



License
-------

Copyright 2016-2017 Galaxy IUC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
-------

This material is based upon work supported by the National Science Foundation under Grant Number (Award 1565146)
