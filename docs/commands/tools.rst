tools
=====

This section is auto-generated from the help text for the parsec command
``tools``.


``get_tool_panel`` command
--------------------------

**Usage**::

    parsec tools get_tool_panel [OPTIONS]

**Help**

Get a list of available tool elements in Galaxy's configured toolbox.


**Output**


    List containing tools (if not in sections) or tool sections
            with nested tool descriptions.

   .. seealso:: bioblend.galaxy.toolshed.get_repositories()
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_tools`` command
---------------------

**Usage**::

    parsec tools get_tools [OPTIONS]

**Help**

Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.


**Output**


    List of tool descriptions.

   .. seealso:: bioblend.galaxy.toolshed.get_repositories()
    
**Options**::


      --tool_id TEXT  id of the requested tool
      --name TEXT     name of the requested tool(s)
      --trackster     whether to return only tools that are compatible with
                      Trackster
      -h, --help      Show this message and exit.
    

``install_dependencies`` command
--------------------------------

**Usage**::

    parsec tools install_dependencies [OPTIONS] TOOL_ID

**Help**

Install dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available since Galaxy release_16.10 and is available only to Galaxy admins.


**Output**


    Tool requirement status
    
**Options**::


      -h, --help  Show this message and exit.
    

``paste_content`` command
-------------------------

**Usage**::

    parsec tools paste_content [OPTIONS] CONTENT HISTORY_ID

**Help**

Upload a string to a new dataset in the history specified by ``history_id``.


**Output**


    Information about the created upload job

   See :meth:`upload_file` for the optional parameters.
    
**Options**::


      -h, --help  Show this message and exit.
    

``put_url`` command
-------------------

**Usage**::

    parsec tools put_url [OPTIONS] CONTENT HISTORY_ID

**Help**

Upload a string to a new dataset in the history specified by ``history_id``.


**Output**


    Information about the created upload job

   See :meth:`upload_file` for the optional parameters.
    
**Options**::


      -h, --help  Show this message and exit.
    

``run_tool`` command
--------------------

**Usage**::

    parsec tools run_tool [OPTIONS] HISTORY_ID TOOL_ID TOOL_INPUTS

**Help**

Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.


**Output**


    Information about outputs and job
     For example::

       {
         "outputs": [
           {
             "misc_blurb": "queued",
             "peek": null,
             "update_time": "2019-05-08T12:26:16.069798",
             "data_type": "galaxy.datatypes.tabular.Tabular",
             "tags": [],
             "deleted": false,
             "history_id": "df8fe5ddadbf3ab1",
             "metadata_column_names": null,
             "metadata_delimiter": "	",
             "visible": true,
             "genome_build": "?",
             "create_time": "2019-05-08T12:26:15.997739",
             "hid": 42,
             "file_size": 0,
             "metadata_data_lines": null,
             "file_ext": "tabular",
             "id": "aeb65580396167f3",
             "misc_info": null,
             "hda_ldda": "hda",
             "history_content_type": "dataset",
             "name": "Cut on data 1",
             "metadata_columns": null,
             "uuid": "d91d10af-7546-45be-baa9-902010661466",
             "state": "new",
             "metadata_comment_lines": null,
             "model_class": "HistoryDatasetAssociation",
             "metadata_dbkey": "?",
             "output_name": "out_file1",
             "purged": false,
             "metadata_column_types": null
           }
         ],
         "implicit_collections": [],
         "jobs": [
           {
             "tool_id": "cut1",
             "update_time": "2019-05-08T12:26:16.067389",
             "exit_code": null,
             "state": "new",
             "create_time": "2019-05-08T12:26:16.067372",
             "model_class": "Job",
             "id": "7dd125b61b35d782"
           }
         ],
         "output_collections": []
       }

   The ``tool_inputs`` dict should contain input datasets and parameters
   in the (largely undocumented) format used by the Galaxy API.
   Some examples can be found in `Galaxy's API test suite
   <https://github.com/galaxyproject/galaxy/blob/dev/test/api/test_tools.py>`_.
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_tool`` command
---------------------

**Usage**::

    parsec tools show_tool [OPTIONS] TOOL_ID

**Help**

Get details of a given tool.


**Output**


    Information about the tool's interface
    
**Options**::


      --io_details    whether to get also input and output details
      --link_details  whether to get also link details
      -h, --help      Show this message and exit.
    

``upload_file`` command
-----------------------

**Usage**::

    parsec tools upload_file [OPTIONS] PATH HISTORY_ID

**Help**

Upload the file specified by ``path`` to the history specified by ``history_id``.


**Output**


    Information about the created upload job
    
**Options**::


      --dbkey TEXT      (optional) genome dbkey
      --file_name TEXT  (optional) name of the new history dataset
      --file_type TEXT  (optional) Galaxy datatype for the new dataset, default is
                        auto
      --space_to_tab    whether to convert spaces to tabs. Default is ``False``.
                        Applicable only if to_posix_lines is ``True``
      --to_posix_lines  if ``True`` (the default), convert universal line endings to
                        POSIX line endings. Set to ``False`` when uploading a gzip,
                        bz2 or zip archive containing a binary file
      -h, --help        Show this message and exit.
    

``upload_from_ftp`` command
---------------------------

**Usage**::

    parsec tools upload_from_ftp [OPTIONS] PATH HISTORY_ID

**Help**

Upload the file specified by ``path`` from the user's FTP directory to the history specified by ``history_id``.


**Output**


    Information about the created upload job
    
**Options**::


      -h, --help  Show this message and exit.
    
