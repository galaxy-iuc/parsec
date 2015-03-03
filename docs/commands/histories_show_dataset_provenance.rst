
``histories_show_dataset_provenance`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_show_dataset_provenance``. This help message can be generated with ``parsec histories_show_dataset_provenance
--help``.

**Usage**::

    parsec histories_show_dataset_provenance [OPTIONS] HISTORY_ID

**Help**

Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --follow                If ``follow`` is ``True``, recursively fetch dataset
                              provenance information for all inputs and their
                              inputs, etc....
      --help                  Show this message and exit.
    
