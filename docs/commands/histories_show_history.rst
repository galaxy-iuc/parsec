
``histories_show_history`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_show_history``. This help message can be generated with ``parsec histories_show_history
--help``.

**Usage**::

    parsec histories_show_history [OPTIONS] HISTORY_ID

**Help**

Get details of a given history. By default, just get the history meta information.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --contents TEXT         When true, the complete list of datasets in the
                              given history.
      --deleted TEXT          Used when contents=True, includes deleted datasets
                              is history dataset list
      --visible TEXT          Used when contents=True, includes only visible
                              datasets is history dataset list
      --details TEXT          Used when contents=True, includes dataset details.
                              Set to 'all' for the most information
      --types TEXT            ???
      --help                  Show this message and exit.
    
