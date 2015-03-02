
``folders_delete_folder`` command
===============================

This section is auto-generated from the help text for the parsec command
``folders_delete_folder``. This help message can be generated with ``parsec folders_delete_folder
--help``.

**Usage**::

    parsec folders_delete_folder [OPTIONS] FOLDER_ID

**Help**

Marks the folder with the given ``id`` as `deleted` (or removes the `deleted` mark if the `undelete` param is True).

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --undelete              If set to True, the folder will be undeleted (i.e.
                              the `deleted` mark will be removed)
      --help                  Show this message and exit.
    
