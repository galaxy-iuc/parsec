histories
=========

This section is auto-generated from the help text for the parsec command
``histories``.


``create_dataset_collection`` command
-------------------------------------

**Usage**::

    parsec histories create_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Create a new dataset collection


**Output**


    
    
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


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_history`` command
--------------------------

**Usage**::

    parsec histories delete_history [OPTIONS] HISTORY_ID

**Help**

Delete a history.


**Output**


    
    
**Options**::


      --purge     if ``True``, also purge (permanently delete) the history
      -h, --help  Show this message and exit.
    

``download_dataset`` command
----------------------------

**Usage**::

    parsec histories download_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

.. deprecated:: 0.8.0 Use :meth:`~bioblend.galaxy.datasets.DatasetClient.download_dataset` instead.


**Output**


    
    
**Options**::


      --use_default_filename TEXT  [default: True]
      -h, --help                   Show this message and exit.
    

``download_history`` command
----------------------------

**Usage**::

    parsec histories download_history [OPTIONS] HISTORY_ID JEHA_ID OUTF

**Help**

Download a history export archive.  Use :meth:`export_history` to create an export.


**Output**


    
    
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
      -h, --help         Show this message and exit.
    

``get_current_history`` command
-------------------------------

**Usage**::

    parsec histories get_current_history [OPTIONS]

**Help**

.. deprecated:: 0.5.2 Use :meth:`get_most_recently_used_history` instead.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_histories`` command
-------------------------

**Usage**::

    parsec histories get_histories [OPTIONS]

**Help**

Get all histories or filter the specific one(s) via the provided ``name`` or ``history_id``. Provide only one argument, ``name`` or ``history_id``, but not both.


**Output**


    Return a list of history element dicts. If more than one
            history matches the given ``name``, return the list of all the
            histories with the given name
    
**Options**::


      --history_id TEXT  Encoded history ID to filter on
      --name TEXT        Name of history to filter on
      --deleted TEXT
      -h, --help         Show this message and exit.
    

``get_most_recently_used_history`` command
------------------------------------------

**Usage**::

    parsec histories get_most_recently_used_history [OPTIONS]

**Help**

Returns the current user's most recently used history (not deleted).


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

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
    

``show_dataset`` command
------------------------

**Usage**::

    parsec histories show_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Get details about a given history dataset.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_dataset_collection`` command
-----------------------------------

**Usage**::

    parsec histories show_dataset_collection [OPTIONS] HISTORY_ID

**Help**

Get details about a given history dataset collection.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_dataset_provenance`` command
-----------------------------------

**Usage**::

    parsec histories show_dataset_provenance [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).


**Output**


    
    
**Options**::


      --follow    If ``follow`` is ``True``, recursively fetch dataset provenance
                  information for all inputs and their inputs, etc...
      -h, --help  Show this message and exit.
    

``show_history`` command
------------------------

**Usage**::

    parsec histories show_history [OPTIONS] HISTORY_ID

**Help**

Get details of a given history. By default, just get the history meta information.


**Output**


    details of the given history
    
**Options**::


      --contents      When ``True``, the complete list of datasets in the given
                      history.
      --deleted TEXT  Used when contents=True, includes deleted datasets in history
                      dataset list
      --visible TEXT  Used when contents=True, includes only visible datasets in
                      history dataset list
      --details TEXT  Used when contents=True, includes dataset details. Set to
                      'all' for the most information
      --types TEXT    ???
      -h, --help      Show this message and exit.
    

``show_matching_datasets`` command
----------------------------------

**Usage**::

    parsec histories show_matching_datasets [OPTIONS] HISTORY_ID

**Help**

Get dataset details for matching datasets within a history.


**Output**


    
    
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


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_dataset`` command
--------------------------

**Usage**::

    parsec histories update_dataset [OPTIONS] HISTORY_ID DATASET_ID

**Help**

Update history dataset metadata. Some of the attributes that can be modified are documented below.


**Output**


    details of the updated dataset (for Galaxy release_15.01 and
       earlier only the updated attributes)

   .. warning::
       The return value was changed in BioBlend v0.8.0, previously it was
       the status code (type int).
    
**Options**::


      --annotation TEXT    Replace history dataset annotation with given string
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

   .. warning::
       The return value was changed in BioBlend v0.8.0, previously it was
       the status code (type int).
    
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


    details of the updated history (for Galaxy release_15.01 and
       earlier only the updated attributes)

   .. warning::
       The return value was changed in BioBlend v0.8.0, previously it was
       the status code (type int).
    
**Options**::


      --annotation TEXT  Replace history annotation with given string
      --deleted          Mark or unmark history as deleted
      --importable       Mark or unmark history as importable
      --name TEXT        Replace history name with the given string
      --published        Mark or unmark history as published
      --purged           If True, mark history as purged (permanently deleted).
                         Ignored on Galaxy release_15.01 and earlier
      --tags TEXT        Replace history tags with the given list
      -h, --help         Show this message and exit.
    

``upload_dataset_from_library`` command
---------------------------------------

**Usage**::

    parsec histories upload_dataset_from_library [OPTIONS] HISTORY_ID

**Help**

Upload a dataset into the history from a library. Requires the library dataset ID, which can be obtained from the library contents.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    
