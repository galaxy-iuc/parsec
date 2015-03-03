
``libraries_get_libraries`` command
===============================

This section is auto-generated from the help text for the parsec command
``libraries_get_libraries``. This help message can be generated with ``parsec libraries_get_libraries
--help``.

**Usage**::

    parsec libraries_get_libraries [OPTIONS]

**Help**

Get all the libraries or filter for specific one(s) via the provided name or ID. Provide only one argument: ``name`` or ``library_id``, but not both.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --library_id TEXT       filter for library by library id
      --name TEXT             If ``name`` is set and multiple names match the
                              given name, all the libraries matching the argument
                              will be returned.
      --deleted               If set to ``True``, return libraries that have been
                              deleted.
      --help                  Show this message and exit.
    
