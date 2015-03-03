
``histories_download_history`` command
===============================

This section is auto-generated from the help text for the parsec command
``histories_download_history``. This help message can be generated with ``parsec histories_download_history
--help``.

**Usage**::

    parsec histories_download_history [OPTIONS] HISTORY_ID JEHA_ID OUTF

**Help**

Download a history export archive.  Use :meth:`export_history` to create an export.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --chunk_size INTEGER    how many bytes at a time should be read into memory
      --help                  Show this message and exit.
    
