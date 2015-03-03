
``workflows_get_workflows`` command
===============================

This section is auto-generated from the help text for the parsec command
``workflows_get_workflows``. This help message can be generated with ``parsec workflows_get_workflows
--help``.

**Usage**::

    parsec workflows_get_workflows [OPTIONS]

**Help**

Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.

**Options**::


      --galaxy_instance TEXT  name of galaxy instance per ~/.planemo.yml
                              [required]
      --workflow_id TEXT      Encoded workflow ID (incompatible with ``name``)
      --name TEXT             Filter by name of workflow (incompatible with
                              ``workflow_id``). If multiple names match the given
                              name, all the workflows matching the argument will
                              be returned.
      --deleted               If set to ``True``, return workflows that have been
                              deleted.
      --published             If set to ``True``, return published workflows.
      --help                  Show this message and exit.
    
