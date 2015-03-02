
``histories_show_matching_datasets`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_show_matching_datasets``. This help message can be generated with ``parsec histories_show_matching_datasets
--help``.

**Usage**::

    parsec histories_show_matching_datasets [OPTIONS] HISTORY_ID

**Help**

Get dataset details for matching datasets within a history.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --name_filter TEXT      Only datasets whose name matches the ``name_filter``
                              regular expression will be returned; use plain
                              strings for exact matches and None to match all
                              datasets in the history.
      --help                  Show this message and exit.
    
