
``histories_get_histories`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_get_histories``. This help message can be generated with ``parsec histories_get_histories
--help``.

**Usage**::

    parsec histories_get_histories [OPTIONS]

**Help**

Get all histories or filter the specific one(s) via the provided ``name`` or ``history_id``. Provide only one argument, ``name`` or ``history_id``, but not both.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --history_id TEXT       Encoded history ID to filter on
      --name TEXT             Name of history to filter on
      --deleted TEXT          None
      --help                  Show this message and exit.
    
