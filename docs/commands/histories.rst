histories
=========

This section is auto-generated from the help text for the parsec command
``histories``.


``copy_content`` command
------------------------

**Usage**::

    parsec histories copy_content [OPTIONS] HISTORY_ID CONTENT_ID

**Help**

Copy existing content (e.g. a dataset) to a history.


**Output**


    Information about the copied content

**Options**::


      --source TEXT  Source of the content to be copied: 'hda' (for a history
                     dataset, the default), 'hdca' (for a dataset collection),
                     'library' (for a library dataset) or 'library_folder' (for all
                     datasets in a library folder).  [default: hda]
      -h, --help     Show this message and exit.


``copy_dataset`` command
------------------------

**Usage**::

    parsec histories copy_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Copy a dataset to a history.


**Output**


    Information about the copied dataset

**Options**::


      --source TEXT  Source of the dataset to be copied: 'hda' (the default),
                     'library' or 'library_folder'  [default: hda]
      -h, --help     Show this message and exit.


``create_dataset_collection`` command
-------------------------------------

**Usage**::

    parsec histories create_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Create a new dataset collection


**Output**


    Information about the new HDCA

**Options**::


      -h, --help  Show this message and exit.


``create_history`` command
--------------------------

**Usage**::

    parsec histories create_history [OPTIONS]

**Help**

Create a new history, optionally setting the ``name``.


**Output**


    Dictionary containing information about newly created history

**Options**::


      --name TEXT  Optional name for new history
      -h, --help   Show this message and exit.


``create_history_tag`` command
------------------------------

**Usage**::

    parsec histories create_history_tag [OPTIONS] HISTORY_ID TAG

**Help**

Create history tag


**Output**


    A dictionary with information regarding the tag.
     For example::

       {'id': 'f792763bee8d277a',
        'model_class': 'HistoryTagAssociation',
        'user_tname': 'NGS_PE_RUN',
        'user_value': None}

**Options**::


      -h, --help  Show this message and exit.


``delete_dataset`` command
--------------------------

**Usage**::

    parsec histories delete_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Mark corresponding dataset as deleted.


**Output**


    None

   .. note::
       For the purge option to work, the Galaxy instance must have the
       ``allow_user_dataset_purge`` option set to ``true`` in the
       ``config/galaxy.yml`` configuration file.

**Options**::


      --purge     if ``True``, also purge (permanently delete) the dataset
      -h, --help  Show this message and exit.


``delete_dataset_collection`` command
-------------------------------------

**Usage**::

    parsec histories delete_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Mark corresponding dataset collection as deleted.


**Output**


    None

**Options**::


      -h, --help  Show this message and exit.


``delete_history`` command
--------------------------

**Usage**::

    parsec histories delete_history [OPTIONS] HISTORY_ID

**Help**

Delete a history.


**Output**


    An error object if an error occurred or a dictionary
            containing: ``id`` (the encoded id of the history), ``deleted`` (if the
            history was marked as deleted), ``purged`` (if the history was
            purged).

   .. note::
     For the purge option to work, the Galaxy instance must have the
     ``allow_user_dataset_purge`` option set to ``true`` in the
     ``config/galaxy.yml`` configuration file.

**Options**::


      --purge     if ``True``, also purge (permanently delete) the history
      -h, --help  Show this message and exit.


``download_history`` command
----------------------------

**Usage**::

    parsec histories download_history [OPTIONS] HISTORY_ID JEHA_ID OUTF

**Help**

Download a history export archive.  Use :meth:`export_history` to create an export.


**Output**


    None

**Options**::


      --chunk_size INTEGER  how many bytes at a time should be read into memory
                            [default: 4096]
      -h, --help            Show this message and exit.


``export_history`` command
--------------------------

**Usage**::

    parsec histories export_history [OPTIONS] HISTORY_ID

**Help**

Start a job to create an export archive for the given history.


**Output**


    ``jeha_id`` of the export, or empty if ``wait`` is ``False``
     and the export is not ready.

**Options**::


      --gzip             create .tar.gz archive if ``True``, else .tar  [default:
                         True]
      --include_hidden   whether to include hidden datasets in the export
      --include_deleted  whether to include deleted datasets in the export
      --wait             if ``True``, block until the export is ready; else, return
                         immediately
      --maxwait FLOAT    Total time (in seconds) to wait for the export to become
                         ready. When set, implies that ``wait`` is ``True``.
      -h, --help         Show this message and exit.


``get_histories`` command
-------------------------

**Usage**::

    parsec histories get_histories [OPTIONS]

**Help**

Get all histories, or select a subset by specifying optional arguments for filtering (e.g. a history name).


**Output**


    List of history dicts.

**Options**::


      --history_id TEXT  Encoded history ID to filter on
      --name TEXT        History name to filter on.
      --deleted          whether to filter for the deleted histories (``True``) or
                         for the non-deleted ones (``False``)
      --published TEXT   whether to filter for the published histories (``True``) or
                         for the non-published ones (``False``). If not set, no
                         filtering is applied. Note the filtering is only applied to
                         the user's own histories; to access all histories published
                         by any user, use the ``get_published_histories`` method.
      --slug TEXT        History slug to filter on
      -h, --help         Show this message and exit.


``get_most_recently_used_history`` command
------------------------------------------

**Usage**::

    parsec histories get_most_recently_used_history [OPTIONS]

**Help**

Returns the current user's most recently used history (not deleted).


**Output**


    History representation

**Options**::


      -h, --help  Show this message and exit.


``get_published_histories`` command
-----------------------------------

**Usage**::

    parsec histories get_published_histories [OPTIONS]

**Help**

Get all published histories (by any user), or select a subset by specifying optional arguments for filtering (e.g. a history name).


**Output**


    List of history dicts.

**Options**::


      --name TEXT  History name to filter on.
      --deleted    whether to filter for the deleted histories (``True``) or for the
                   non-deleted ones (``False``)
      --slug TEXT  History slug to filter on
      -h, --help   Show this message and exit.


``get_status`` command
----------------------

**Usage**::

    parsec histories get_status [OPTIONS] HISTORY_ID

**Help**

Returns the state of this history


**Output**


    A dict documenting the current state of the history. Has the following keys:
       'state' = This is the current state of the history, such as ok, error, new etc.
       'state_details' = Contains individual statistics for various dataset states.
       'percent_complete' = The overall number of datasets processed to completion.

**Options**::


      -h, --help  Show this message and exit.


``import_history`` command
--------------------------

**Usage**::

    parsec histories import_history [OPTIONS]

**Help**

Import a history from an archive on disk or a URL.


**Output**




**Options**::


      --file_path TEXT  Path to exported history archive on disk. :type url: str
                        :param url: URL for an exported history archive
      --url TEXT
      -h, --help        Show this message and exit.


``open_history`` command
------------------------

**Usage**::

    parsec histories open_history [OPTIONS] HISTORY_ID

**Help**

Open Galaxy in a new tab of the default web browser and switch to the specified history.


**Output**


    ``None``

   .. warning::
     After opening the specified history, all previously opened Galaxy tabs
     in the browser session will have the current history changed to this
     one, even if the interface still shows another history. Refreshing
     any such tab is recommended.

**Options**::


      -h, --help  Show this message and exit.


``show_dataset`` command
------------------------

**Usage**::

    parsec histories show_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Get details about a given history dataset.


**Output**


    Information about the dataset

**Options**::


      -h, --help  Show this message and exit.


``show_dataset_collection`` command
-----------------------------------

**Usage**::

    parsec histories show_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Get details about a given history dataset collection.


**Output**


    Information about the dataset collection

**Options**::


      -h, --help  Show this message and exit.


``show_dataset_provenance`` command
-----------------------------------

**Usage**::

    parsec histories show_dataset_provenance [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).


**Output**


    Dataset provenance information
     For example::

       {'id': '6fbd9b2274c62ebe',
        'job_id': '5471ba76f274f929',
        'parameters': {'chromInfo': '"/usr/local/galaxy/galaxy-dist/tool-data/shared/ucsc/chrom/mm9.len"',
                       'dbkey': '"mm9"',
                       'experiment_name': '"H3K4me3_TAC_MACS2"',
                       'input_chipseq_file1': {'id': '6f0a311a444290f2',
                                               'uuid': 'null'},
                       'input_control_file1': {'id': 'c21816a91f5dc24e',
                                               'uuid': '16f8ee5e-228f-41e2-921e-a07866edce06'},
                       'major_command': '{"gsize": "2716965481.0", "bdg": "False", "__current_case__": 0, "advanced_options": {"advanced_options_selector": "off", "__current_case__": 1}, "input_chipseq_file1": 104715, "xls_to_interval": "False", "major_command_selector": "callpeak", "input_control_file1": 104721, "pq_options": {"pq_options_selector": "qvalue", "qvalue": "0.05", "__current_case__": 1}, "bw": "300", "nomodel_type": {"nomodel_type_selector": "create_model", "__current_case__": 1}}'},
        'stderr': '',
        'stdout': '',
        'tool_id': 'toolshed.g2.bx.psu.edu/repos/ziru-zhou/macs2/modencode_peakcalling_macs2/2.0.10.2',
        'uuid': '5c0c43f5-8d93-44bd-939d-305e82f213c6'}

**Options**::


      --follow    If ``True``, recursively fetch dataset provenance information for
                  all inputs and their inputs, etc.
      -h, --help  Show this message and exit.


``show_history`` command
------------------------

**Usage**::

    parsec histories show_history [OPTIONS] HISTORY_ID

**Help**

Get details of a given history. By default, just get the history meta information.


**Output**


    details of the given history or list of dataset info

   .. note::
       As an alternative to using the ``contents=True`` parameter, consider
       using ``gi.datasets.get_datasets(history_id=history_id)`` which offers
       more extensive functionality for filtering and ordering the results.

**Options**::


      --contents      When ``True``, instead of the history details, return a list
                      with info for all datasets in the given history. Note that
                      inside each dataset info dict, the id which should be used for
                      further requests about this history dataset is given by the
                      value of the `id` (not `dataset_id`) key.
      --deleted TEXT  When ``contents=True``, whether to filter for the deleted
                      datasets (``True``) or for the non-deleted ones (``False``).
                      If not set, no filtering is applied.
      --visible TEXT  When ``contents=True``, whether to filter for the visible
                      datasets (``True``) or for the hidden ones (``False``). If not
                      set, no filtering is applied.
      --details TEXT  When ``contents=True``, include dataset details. Set to 'all'
                      for the most information.
      --types TEXT    When ``contents=True``, filter for history content types. If
                      set to ``['dataset']``, return only datasets. If set to
                      ``['dataset_collection']``, return only dataset collections.
                      If not set, no filtering is applied.
      -h, --help      Show this message and exit.


``show_matching_datasets`` command
----------------------------------

**Usage**::

    parsec histories show_matching_datasets [OPTIONS] HISTORY_ID

**Help**

Get dataset details for matching datasets within a history.


**Output**


    List of dictionaries

**Options**::


      --name_filter TEXT  Only datasets whose name matches the ``name_filter``
                          regular expression will be returned; use plain strings for
                          exact matches and None to match all datasets in the
                          history
      -h, --help          Show this message and exit.


``undelete_history`` command
----------------------------

**Usage**::

    parsec histories undelete_history [OPTIONS] HISTORY_ID

**Help**

Undelete a history


**Output**


    'OK' if it was deleted

**Options**::


      -h, --help  Show this message and exit.


``update_dataset`` command
--------------------------

**Usage**::

    parsec histories update_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Update history dataset metadata. Some of the attributes that can be modified are documented below.


**Output**


    details of the updated dataset

   .. versionchanged:: 0.8.0
       Changed the return value from the status code (type int) to a dict.

**Options**::


      --annotation TEXT    Replace history dataset annotation with given string
      --datatype TEXT      Replace the datatype of the history dataset with the
                           given string. The string must be a valid Galaxy datatype,
                           both the current and the target datatypes must allow
                           datatype changes, and the dataset must not be in use as
                           input or output of a running job (including uploads),
                           otherwise an error will be raised.
      --deleted            Mark or unmark history dataset as deleted
      --genome_build TEXT  Replace history dataset genome build (dbkey)
      --name TEXT          Replace history dataset name with the given string
      --visible            Mark or unmark history dataset as visible
      -h, --help           Show this message and exit.


``update_dataset_collection`` command
-------------------------------------

**Usage**::

    parsec histories update_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Update history dataset collection metadata. Some of the attributes that can be modified are documented below.


**Output**


    the updated dataset collection attributes

   .. versionchanged:: 0.8.0
       Changed the return value from the status code (type int) to a dict.

**Options**::


      --deleted    Mark or unmark history dataset collection as deleted
      --name TEXT  Replace history dataset collection name with the given string
      --visible    Mark or unmark history dataset collection as visible
      -h, --help   Show this message and exit.


``update_history`` command
--------------------------

**Usage**::

    parsec histories update_history [OPTIONS] HISTORY_ID

**Help**

Update history metadata information. Some of the attributes that can be modified are documented below.


**Output**


    details of the updated history

   .. versionchanged:: 0.8.0
       Changed the return value from the status code (type int) to a dict.

**Options**::


      --annotation TEXT  Replace history annotation with given string
      --deleted          Mark or unmark history as deleted
      --importable       Mark or unmark history as importable
      --name TEXT        Replace history name with the given string
      --published        Mark or unmark history as published
      --purged           If ``True``, mark history as purged (permanently deleted).
      --tags TEXT        Replace history tags with the given list
      -h, --help         Show this message and exit.


``upload_dataset_from_library`` command
---------------------------------------

**Usage**::

    parsec histories upload_dataset_from_library [OPTIONS] HISTORY_ID

**Help**

Upload a dataset into the history from a library. Requires the library dataset ID, which can be obtained from the library contents.


**Output**


    Information about the newly created HDA

**Options**::


      -h, --help  Show this message and exit.

