
``libraries_upload_file_from_server`` command
===============================

This section is auto-generated from the help text for the parsec command
``libraries_upload_file_from_server``. This help message can be generated with ``parsec libraries_upload_file_from_server
--help``.

**Usage**::

    parsec libraries_upload_file_from_server [OPTIONS] LIBRARY_ID

**Help**

Upload all files in the specified subdirectory of the Galaxy library import directory to a library.

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
    
