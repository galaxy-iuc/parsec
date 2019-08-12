toolShed
========

This section is auto-generated from the help text for the parsec command
``toolShed``.


``get_repositories`` command
----------------------------

**Usage**::

    parsec toolShed get_repositories [OPTIONS]

**Help**

Get the list of all installed Tool Shed repositories on this Galaxy instance.


**Output**


    a list of dictionaries containing information about
     repositories present in the Tool Shed.
     For example::

       [{u'changeset_revision': u'4afe13ac23b6',
         u'deleted': False,
         u'dist_to_shed': False,
         u'error_message': u'',
         u'name': u'velvet_toolsuite',
         u'owner': u'edward-kirton',
         u'status': u'Installed'}]

   .. versionchanged:: 0.4.1
       Changed method name from ``get_tools`` to ``get_repositories`` to
       better align with the Tool Shed concepts

   .. seealso:: bioblend.galaxy.tools.get_tool_panel()
    
**Options**::


      -h, --help  Show this message and exit.
    

``install_repository_revision`` command
---------------------------------------

**Usage**::

    parsec toolShed install_repository_revision [OPTIONS] TOOL_SHED_URL NAME

**Help**

Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed through the Tool Shed, (use ``install_tool_dependencies`` or ``install_repository_dependencies``) or through a resolver that supports installing dependencies (use ``install_resolver_dependencies``). Note that any combination of the three dependency resolving variables is valid.


**Output**


    
    
**Options**::


      --install_tool_dependencies     Whether or not to automatically handle tool
                                      dependencies (see
                                      https://galaxyproject.org/toolshed/tool-
                                      dependency-recipes/ for more details)
      --install_repository_dependencies
                                      Whether or not to automatically handle
                                      repository dependencies (see
                                      https://galaxyproject.org/toolshed/defining-
                                      repository-dependencies/ for more details)
      --install_resolver_dependencies
                                      Whether or not to automatically install
                                      resolver dependencies (e.g. conda). This
                                      parameter is silently ignored in Galaxy
                                      ``release_16.04`` and earlier.
      --tool_panel_section_id TEXT    The ID of the Galaxy tool panel section where
                                      the tool should be insterted under. Note that
                                      you should specify either this parameter or
                                      the ``new_tool_panel_section_label``. If both
                                      are specified, this one will take precedence.
      --new_tool_panel_section_label TEXT
                                      The name of a Galaxy tool panel section that
                                      should be created and the repository installed
                                      into.
      -h, --help                      Show this message and exit.
    

``show_repository`` command
---------------------------

**Usage**::

    parsec toolShed show_repository [OPTIONS] TOOLSHED_ID

**Help**

Get details of a given Tool Shed repository as it is installed on this Galaxy instance.


**Output**


    Information about the tool
     For example::

       {u'changeset_revision': u'b17455fb6222',
        u'ctx_rev': u'8',
        u'owner': u'aaron',
        u'status': u'Installed',
        u'url': u'/api/tool_shed_repositories/82de4a4c7135b20a'}

   .. versionchanged:: 0.4.1
       Changed method name from ``show_tool`` to ``show_repository`` to
       better align with the Tool Shed concepts
    
**Options**::


      -h, --help  Show this message and exit.
    

``uninstall_repository_revision`` command
-----------------------------------------

**Usage**::

    parsec toolShed uninstall_repository_revision [OPTIONS] NAME OWNER

**Help**

Uninstalls a specified repository revision from this Galaxy instance.


**Output**


    If successful, a dictionary with a message noting the removal
    
**Options**::


      --remove_from_disk  whether to also remove the repository from disk (the
                          default) or only deactivate it  [default: True]
      -h, --help          Show this message and exit.
    
