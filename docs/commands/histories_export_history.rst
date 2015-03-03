
``histories_export_history`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_export_history``. This help message can be generated with ``parsec histories_export_history
--help``.

**Usage**::

    parsec histories_export_history [OPTIONS] HISTORY_ID

**Help**

Start a job to create an export archive for the given history.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --gzip                  create .tar.gz archive if :obj:`True`, else .tar
      --include_hidden        whether to include hidden datasets in the export
      --include_deleted       whether to include deleted datasets in the export
      --wait                  if :obj:`True`, block until the export is ready;
                              else, return immediately
      --help                  Show this message and exit.
    
