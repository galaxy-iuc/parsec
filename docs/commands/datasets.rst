datasets
========

This section is auto-generated from the help text for the parsec command
``datasets``.


``download_dataset`` command
----------------------------

**Usage**::

    parsec datasets download_dataset [OPTIONS] DATASET_ID

**Help**

Download a dataset to file or in memory. If the dataset state is not 'ok', a ``DatasetStateException`` will be thrown, unless ``require_ok_state=False``.


**Output**


    If a ``file_path`` argument is not provided, returns a dict containing the file content.
            Otherwise returns nothing.
    
**Options**::


      --file_path TEXT        If this argument is provided, the dataset will be
                              streamed to disk at that path (should be a directory
                              if ``use_default_filename=True``). If the file_path
                              argument is not provided, the dataset content is
                              loaded into memory and returned by the method (Memory
                              consumption may be heavy as the entire file will be in
                              memory).
    
      --use_default_filename  If ``True``, the exported file will be saved as
                              ``file_path/%s``, where ``%s`` is the dataset name. If
                              ``False``, ``file_path`` is assumed to contain the
                              full file path including the filename.  [default:
                              True]
    
      --require_ok_state      If ``False``, datasets will be downloaded even if not
                              in an 'ok' state, issuing a ``DatasetStateWarning``
                              rather than raising a ``DatasetStateException``.
                              [default: True]
    
      --maxwait FLOAT         Total time (in seconds) to wait for the dataset state
                              to become terminal. If the dataset state is not
                              terminal within this time, a
                              ``DatasetTimeoutException`` will be thrown.  [default:
                              12000]
    
      -h, --help              Show this message and exit.
    

``get_datasets`` command
------------------------

**Usage**::

    parsec datasets get_datasets [OPTIONS]

**Help**

Get the latest datasets, or select another subset by specifying optional arguments for filtering (e.g. a history ID).


**Output**


    
    
**Options**::


      --limit INTEGER         Maximum number of datasets to return.  [default: 500]
      --offset INTEGER        Return datasets starting from this specified position.
                              For example, if ``limit`` is set to 100 and ``offset``
                              to 200, datasets 200-299 will be returned.
    
      --name TEXT             Dataset name to filter on.
      --extension TEXT        Dataset extension (or list of extensions) to filter
                              on.
    
      --state TEXT            Dataset state (or list of states) to filter on.
      --visible               Optionally filter datasets by their ``visible``
                              attribute.
    
      --deleted               Optionally filter datasets by their ``deleted``
                              attribute.
    
      --purged                Optionally filter datasets by their ``purged``
                              attribute.
    
      --tool_id TEXT          Tool ID to filter on.
      --tag TEXT              Dataset tag to filter on.
      --history_id TEXT       Encoded history ID to filter on.
      --create_time_min TEXT  Show only datasets created after the provided time and
                              date, which should be formatted as ``YYYY-MM-DDTHH-MM-
                              SS``.
    
      --create_time_max TEXT  Show only datasets created before the provided time
                              and date, which should be formatted as ``YYYY-MM-
                              DDTHH-MM-SS``.
    
      --update_time_min TEXT  Show only datasets last updated after the provided
                              time and date, which should be formatted as ``YYYY-MM-
                              DDTHH-MM-SS``.
    
      --update_time_max TEXT  Show only datasets last updated before the provided
                              time and date, which should be formatted as ``YYYY-MM-
                              DDTHH-MM-SS``.
    
      --order TEXT            One or more of the following attributes for ordering
                              datasets: ``create_time`` (default), ``extension``,
                              ``hid``, ``history_id``, ``name``, ``update_time``.
                              Optionally, ``-asc`` or ``-dsc`` (default) can be
                              appended for ascending and descending order
                              respectively. Multiple attributes can be stacked as a
                              comma-separated list of values, e.g. ``create_time-
                              asc,hid-dsc``.  [default: create_time-dsc]
    
      -h, --help              Show this message and exit.
    

``publish_dataset`` command
---------------------------

**Usage**::

    parsec datasets publish_dataset [OPTIONS] DATASET_ID

**Help**

Make a dataset publicly available or private. For more fine-grained control (assigning different permissions to specific roles), use the ``update_permissions()`` method.


**Output**


    Current roles for all available permission types.

   .. note::
     This method can only be used with Galaxy ``release_19.05`` or later.
    
**Options**::


      --published  Whether to make the dataset published (``True``) or private
                   (``False``).
    
      -h, --help   Show this message and exit.
    

``show_dataset`` command
------------------------

**Usage**::

    parsec datasets show_dataset [OPTIONS] DATASET_ID

**Help**

Get details about a given dataset. This can be a history or a library dataset.


**Output**


    Information about the HDA or LDDA
    
**Options**::


      --deleted        Whether to return results for a deleted dataset
      --hda_ldda TEXT  Whether to show a history dataset ('hda' - the default) or
                       library dataset ('ldda').  [default: hda]
    
      -h, --help       Show this message and exit.
    

``update_permissions`` command
------------------------------

**Usage**::

    parsec datasets update_permissions [OPTIONS] DATASET_ID

**Help**

Set access, manage or modify permissions for a dataset to a list of roles.


**Output**


    Current roles for all available permission types.

   .. note::
     This method can only be used with Galaxy ``release_19.05`` or later.
    
**Options**::


      --access_ids TEXT  role IDs which should have access permissions for the
                         dataset.
    
      --manage_ids TEXT  role IDs which should have manage permissions for the
                         dataset.
    
      --modify_ids TEXT  role IDs which should have modify permissions for the
                         dataset.
    
      -h, --help         Show this message and exit.
    

``wait_for_dataset`` command
----------------------------

**Usage**::

    parsec datasets wait_for_dataset [OPTIONS] DATASET_ID

**Help**

Wait until a dataset is in a terminal state.


**Output**


    Details of the given dataset.
    
**Options**::


      --maxwait FLOAT   Total time (in seconds) to wait for the dataset state to
                        become terminal. If the dataset state is not terminal within
                        this time, a ``DatasetTimeoutException`` will be raised.
                        [default: 12000]
    
      --interval FLOAT  Time (in seconds) to wait between 2 consecutive checks.
                        [default: 3]
    
      --check           Whether to check if the dataset terminal state is 'ok'.
                        [default: True]
    
      -h, --help        Show this message and exit.
    
