
``toolShed_install_repository_revision`` command
===============================

This section is auto-generated from the help text for the parsec command
``toolShed_install_repository_revision``. This help message can be generated with ``parsec toolShed_install_repository_revision
--help``.

**Usage**::

    parsec toolShed_install_repository_revision [OPTIONS] TOOL_SHED_URL

**Help**

Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed, use ``install_tool_dependencies`` or ``install_repository_dependencies``.

**Options**::


      --galaxy_instance TEXT          name of galaxy instance per ~/.planemo.yml
                                      [required]
      --install_tool_dependencies     Whether or not to automatically handle tool
                                      dependencies (see http://wiki.galaxyproject.
                                      org/AToolOrASuitePerRepository for more
                                      details)
      --install_repository_dependencies
                                      Whether or not to automatically handle
                                      repository dependencies (see http://wiki.gal
                                      axyproject.org/DefiningRepositoryDependencie
                                      s for more details)
      --tool_panel_section_id TEXT    The ID of the Galaxy tool panel section
                                      where the tool should be insterted under.
                                      Note that you should specify either this
                                      parameter or the
                                      ``new_tool_panel_section_label``. If both
                                      are specified, this one will take
                                      precedence.
      --new_tool_panel_section_label TEXT
                                      The name of a Galaxy tool panel section that
                                      should be created and the repository
                                      installed into.
      --help                          Show this message and exit.
    
