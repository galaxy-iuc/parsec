
``tools_get_tools`` command
===============================

This section is auto-generated from the help text for the parsec command
``tools_get_tools``. This help message can be generated with ``parsec tools_get_tools
--help``.

**Usage**::

    parsec tools_get_tools [OPTIONS]

**Help**

Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --tool_id TEXT          id of the requested tool
      --name TEXT             name of the requested tool(s)
      --trackster TEXT        if True, only tools that are compatible with
                              Trackster are returned
      --help                  Show this message and exit.
    
