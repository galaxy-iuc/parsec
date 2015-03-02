
``datasets_download_dataset`` command
===============================

This section is auto-generated from the help text for the parsec command
``datasets_download_dataset``. This help message can be generated with ``parsec datasets_download_dataset
--help``.

**Usage**::

    parsec datasets_download_dataset [OPTIONS] DATASET_ID

**Help**

Downloads the dataset identified by 'id'.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --file_path TEXT        If the file_path argument is provided, the dataset
                              will be streamed to disk at that path (Should not
                              contain filename if use_default_name=True). If the
                              file_path argument is not provided, the dataset
                              content is loaded into memory and returned by the
                              method (Memory consumption may be heavy as the
                              entire file will be in memory).
      --use_default_filename  If the use_default_name parameter is True, the
                              exported file will be saved as file_path/%s, where
                              %s is the dataset name. If use_default_name is
                              False, file_path is assumed to contain the full file
                              path including filename.
      --wait_for_completion   If wait_for_completion is True, this call will block
                              until the dataset is ready. If the dataset state
                              becomes invalid, a DatasetStateException will be
                              thrown.
      --maxwait FLOAT         Time (in seconds) to wait for dataset to complete.
                              If the dataset state is not complete within this
                              time, a DatasetTimeoutException will be thrown.
      --file_ext TEXT         Extension to request from Galaxy. Will default to
                              dataset file_ext value. Provided for backwards
                              compatability with HistoryClient.download_dataset()
      --help                  Show this message and exit.
    
