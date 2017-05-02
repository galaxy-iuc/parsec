tools
=====

``get_tool_panel`` command
--------------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools get_tool_panel [OPTIONS]

**Help**

Get a list of available tool elements in Galaxy's configured toolbox.

**Options**::


      --help  Show this message and exit.
    

``get_tools`` command
---------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools get_tools [OPTIONS]

**Help**

Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.

**Options**::


      --tool_id TEXT  id of the requested tool
      --name TEXT     name of the requested tool(s)
      --trackster     if True, only tools that are compatible with Trackster are
                      returned
      --help          Show this message and exit.
    

``install_dependencies`` command
--------------------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools install_dependencies [OPTIONS] TOOL_ID

**Help**

Install dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available since Galaxy release_16.10 and is available only to Galaxy admins.

**Options**::


      --help  Show this message and exit.
    

``paste_content`` command
-------------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools paste_content [OPTIONS] CONTENT HISTORY_ID

**Help**

Upload a string to a new dataset in the history specified by ``history_id``.

**Options**::


      --help  Show this message and exit.
    

``put_url`` command
-------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools put_url [OPTIONS] CONTENT HISTORY_ID

**Help**

Upload a string to a new dataset in the history specified by ``history_id``.

**Options**::


      --help  Show this message and exit.
    

``run_tool`` command
--------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools run_tool [OPTIONS] HISTORY_ID TOOL_ID TOOL_INPUTS

**Help**

Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.

**Options**::


      --help  Show this message and exit.
    

``show_tool`` command
---------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools show_tool [OPTIONS] TOOL_ID

**Help**

Get details of a given tool.

**Options**::


      --io_details    if True, get also input and output details
      --link_details  if True, get also link details
      --help          Show this message and exit.
    

``upload_file`` command
-----------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools upload_file [OPTIONS] PATH HISTORY_ID

**Help**

Upload the file specified by ``path`` to the history specified by ``history_id``.

**Options**::


      --dbkey TEXT      (optional) genome dbkey
      --to_posix_lines  if True, convert universal line endings to POSIX line
                        endings. Default is True. Set to False if you upload a gzip,
                        bz2 or zip archive containing a binary file
      --file_name TEXT  (optional) name of the new history dataset
      --space_to_tab    whether to convert spaces to tabs. Default is False.
                        Applicable only if to_posix_lines is True
      --file_type TEXT  Galaxy datatype for the new dataset, default is auto
      --help            Show this message and exit.
    

``upload_from_ftp`` command
---------------------------

This section is auto-generated from the help text for the parsec command
``tools``.

**Usage**::

    parsec tools upload_from_ftp [OPTIONS] PATH HISTORY_ID

**Help**

Upload the file specified by ``path`` from the user's FTP directory to the history specified by ``history_id``.

**Options**::


      --help  Show this message and exit.
    
