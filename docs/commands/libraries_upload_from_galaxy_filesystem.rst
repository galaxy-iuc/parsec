
``libraries_upload_from_galaxy_filesystem`` command
===============================

This section is auto-generated from the help text for the parsec command
``libraries_upload_from_galaxy_filesystem``. This help message can be generated with ``parsec libraries_upload_from_galaxy_filesystem
--help``.

**Usage**::

    parsec libraries_upload_from_galaxy_filesystem [OPTIONS] LIBRARY_ID

**Help**

Upload a set of files already present on the filesystem of the Galaxy server to a library.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --folder_id TEXT        id of the folder where to place the uploaded files.
                              If not provided, the root folder will be used
      --file_type TEXT        Galaxy file format name
      --dbkey TEXT            Dbkey
      --link_data_only TEXT   either 'copy_files' (default) or 'link_to_files'.
                              Setting to 'link_to_files' symlinks instead of
                              copying the files
      --roles TEXT            ???
      --help                  Show this message and exit.
    
