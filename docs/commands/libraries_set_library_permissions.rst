
``libraries_set_library_permissions`` command
===============================

This section is auto-generated from the help text for the parsec command
``libraries_set_library_permissions``. This help message can be generated with ``parsec libraries_set_library_permissions
--help``.

**Usage**::

    parsec libraries_set_library_permissions [OPTIONS] LIBRARY_ID

**Help**

Sets the permissions for a library.  Note: it will override all security for this library even if you leave out a permission type.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --access_in TEXT        list of user ids
      --modify_in TEXT        list of user ids
      --add_in TEXT           list of user ids
      --manage_in TEXT        list of user ids
      --help                  Show this message and exit.
    
