tools
=====

This section is auto-generated from the help text for the parsec command
``tools``.


``get_citations`` command
-------------------------

**Usage**::

    parsec tools get_citations [OPTIONS] TOOL_ID

**Help**

Get BibTeX citations for a given tool ID.


**Output**




**Options**::


      -h, --help  Show this message and exit.


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

Get all tools, or select a subset by specifying optional arguments for filtering (e.g. a tool name).


**Output**


    List of tool descriptions.

   .. seealso:: bioblend.galaxy.toolshed.get_repositories()

**Options**::


      --tool_id TEXT  id of the requested tool
      --name TEXT     Tool name to filter on.
      --trackster     whether to return only tools that are compatible with
                      Trackster
      -h, --help      Show this message and exit.


``install_dependencies`` command
--------------------------------

**Usage**::

    parsec tools install_dependencies [OPTIONS] TOOL_ID

**Help**

Install dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available only to Galaxy admins.


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


``requirements`` command
------------------------

**Usage**::

    parsec tools requirements [OPTIONS] TOOL_ID

**Help**

Return the resolver status for a specific tool. This functionality is available only to Galaxy admins.


**Output**


    List containing a resolver status dict for each tool
     requirement. For example::

       [{'cacheable': False,
         'dependency_resolver': {'auto_init': True,
                                 'auto_install': False,
                                 'can_uninstall_dependencies': True,
                                 'ensure_channels': 'iuc,conda-forge,bioconda,defaults',
                                 'model_class': 'CondaDependencyResolver',
                                 'prefix': '/mnt/galaxy/tool_dependencies/_conda',
                                 'resolver_type': 'conda',
                                 'resolves_simple_dependencies': True,
                                 'use_local': False,
                                 'versionless': False},
         'dependency_type': 'conda',
         'environment_path': '/mnt/galaxy/tool_dependencies/_conda/envs/__blast@2.10.1',
         'exact': True,
         'model_class': 'MergedCondaDependency',
         'name': 'blast',
         'version': '2.10.1'}]

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

       {'implicit_collections': [],
        'jobs': [{'create_time': '2019-05-08T12:26:16.067372',
                  'exit_code': None,
                  'id': '7dd125b61b35d782',
                  'model_class': 'Job',
                  'state': 'new',
                  'tool_id': 'cut1',
                  'update_time': '2019-05-08T12:26:16.067389'}],
        'output_collections': [],
        'outputs': [{'create_time': '2019-05-08T12:26:15.997739',
                     'data_type': 'galaxy.datatypes.tabular.Tabular',
                     'deleted': False,
                     'file_ext': 'tabular',
                     'file_size': 0,
                     'genome_build': '?',
                     'hda_ldda': 'hda',
                     'hid': 42,
                     'history_content_type': 'dataset',
                     'history_id': 'df8fe5ddadbf3ab1',
                     'id': 'aeb65580396167f3',
                     'metadata_column_names': None,
                     'metadata_column_types': None,
                     'metadata_columns': None,
                     'metadata_comment_lines': None,
                     'metadata_data_lines': None,
                     'metadata_dbkey': '?',
                     'metadata_delimiter': '	',
                     'misc_blurb': 'queued',
                     'misc_info': None,
                     'model_class': 'HistoryDatasetAssociation',
                     'name': 'Cut on data 1',
                     'output_name': 'out_file1',
                     'peek': None,
                     'purged': False,
                     'state': 'new',
                     'tags': [],
                     'update_time': '2019-05-08T12:26:16.069798',
                     'uuid': 'd91d10af-7546-45be-baa9-902010661466',
                     'visible': True}]}

   The ``tool_inputs`` dict should contain input datasets and parameters
   in the (largely undocumented) format used by the Galaxy API.
   Some examples can be found in `Galaxy's API test suite
   <https://github.com/galaxyproject/galaxy/blob/dev/lib/galaxy_test/api/test_tools.py>`_.

**Options**::


      --input_format TEXT  input format for the payload. Possible values are the
                           default 'legacy' (where inputs nested inside conditionals
                           or repeats are identified with e.g.
                           '<conditional_name>|<input_name>') or '21.01' (where
                           inputs inside conditionals or repeats are nested
                           elements).  [default: legacy]
      -h, --help           Show this message and exit.


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


``uninstall_dependencies`` command
----------------------------------

**Usage**::

    parsec tools uninstall_dependencies [OPTIONS] TOOL_ID

**Help**

Uninstall dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available only to Galaxy admins.


**Output**


    Tool requirement status

**Options**::


      -h, --help  Show this message and exit.


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

