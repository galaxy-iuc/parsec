
``libraries_get_folders`` command
===============================

This section is auto-generated from the help text for the parsec command
``libraries_get_folders``. This help message can be generated with ``parsec libraries_get_folders
--help``.

**Usage**::

    parsec libraries_get_folders [OPTIONS] LIBRARY_ID

**Help**

Get all the folders or filter specific one(s) via the provided ``name`` or ``folder_id`` in data library with id ``library_id``. Provide only one argument: ``name`` or ``folder_id``, but not both.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --folder_id TEXT        filter for folder by folder id
      --name TEXT             filter for folder by name. For ``name`` specify the
                              full path of the folder starting from the library's
                              root folder, e.g. ``/subfolder/subsubfolder``.
      --deleted               If set to ``True``, return folders that have been
                              deleted.
      --help                  Show this message and exit.
    
