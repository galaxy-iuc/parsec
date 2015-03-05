
``workflows_run_workflow`` command
===============================

This section is auto-generated from the help text for the parsec command
``workflows_run_workflow``. This help message can be generated with ``parsec workflows_run_workflow
--help``.

**Usage**::

    parsec workflows_run_workflow [OPTIONS] WORKFLOW_ID

**Help**

Run the workflow identified by ``workflow_id``

**Options**::


      --galaxy_instance TEXT      name of galaxy instance per ~/.planemo.yml
                                  [required]
      --dataset_map TEXT          A mapping of workflow inputs to datasets. The
                                  datasets source can be a
                                  LibraryDatasetDatasetAssociation (``ldda``),
                                  LibraryDataset (``ld``), or
                                  HistoryDatasetAssociation (``hda``). The map
                                  must be in the following format: ``{'<input>':
                                  {'id': <encoded dataset ID>, 'src': '[ldda, ld,
                                  hda]'}}`` (e.g. ``{'23': {'id':
                                  '29beef4fadeed09f', 'src': 'ld'}}``)
      --params TEXT               A mapping of tool parameters that are non-
                                  datasets parameters. The map must be in the
                                  following format: ``{'blastn': {'param':
                                  'evalue', 'value': '1e-06'}}``
      --history_id TEXT           The encoded history ID where to store the
                                  workflow output. ``history_id`` OR
                                  ``history_name`` should be provided but not
                                  both!
      --history_name TEXT         Create a new history with the given name to
                                  store the workflow output. ``history_id`` OR
                                  ``history_name`` should be provided but not
                                  both!
      --import_inputs_to_history  If ``True``, used workflow inputs will be
                                  imported into the history. If ``False``, only
                                  workflow outputs will be visible in the given
                                  history.
      --replacement_params DICT   pattern-based replacements for post-job actions
                                  (see below)
      --help                      Show this message and exit.
    
