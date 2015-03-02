
``workflows_export_workflow_to_local_path`` command
===============================

This section is auto-generated from the help text for the parsec command
``workflows_export_workflow_to_local_path``. This help message can be generated with ``parsec workflows_export_workflow_to_local_path
--help``.

**Usage**::

    parsec workflows_export_workflow_to_local_path [OPTIONS] WORKFLOW_ID

**Help**

Exports a workflow to a given local path.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --use_default_filename  If the use_default_name parameter is True, the
                              exported file will be saved as file_local_path
                              /Galaxy-Workflow-%s.ga, where %s is the workflow
                              name. If use_default_name is False, file_local_path
                              is assumed to contain the full file path including
                              filename.
      --help                  Show this message and exit.
    
