workflows
=========

This section is auto-generated from the help text for the parsec command
``workflows``.


``cancel_invocation`` command
-----------------------------

**Usage**::

    parsec workflows cancel_invocation [OPTIONS] WORKFLOW_ID INVOCATION_ID

**Help**

Cancel the scheduling of a workflow.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_workflow`` command
---------------------------

**Usage**::

    parsec workflows delete_workflow [OPTIONS] WORKFLOW_ID

**Help**

Delete a workflow identified by `workflow_id`.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``export_workflow_dict`` command
--------------------------------

**Usage**::

    parsec workflows export_workflow_dict [OPTIONS] WORKFLOW_ID

**Help**

Exports a workflow.


**Output**


    Dictionary representing the requested workflow
    
**Options**::


      -h, --help  Show this message and exit.
    

``export_workflow_json`` command
--------------------------------

**Usage**::

    parsec workflows export_workflow_json [OPTIONS] WORKFLOW_ID

**Help**

.. deprecated:: 0.9.0 Use :meth:`export_workflow_dict` instead.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``export_workflow_to_local_path`` command
-----------------------------------------

**Usage**::

    parsec workflows export_workflow_to_local_path [OPTIONS] WORKFLOW_ID

**Help**

Exports a workflow in JSON format to a given local path.


**Output**


    
    
**Options**::


      --use_default_filename  If the use_default_name parameter is True, the
                              exported file will be saved as file_local_path/Galaxy-
                              Workflow-%s.ga, where %s is the workflow name. If
                              use_default_name is False, file_local_path is assumed
                              to contain the full file path including filename.
                              [default: True]
      -h, --help              Show this message and exit.
    

``get_invocations`` command
---------------------------

**Usage**::

    parsec workflows get_invocations [OPTIONS] WORKFLOW_ID

**Help**

Get a list containing all the workflow invocations corresponding to the specified workflow.


**Output**


    A list of workflow invocations.
     For example::

       [{u'history_id': u'2f94e8ae9edff68a',
         u'id': u'df7a1f0c02a5b08e',
         u'model_class': u'WorkflowInvocation',
         u'state': u'new',
         u'update_time': u'2015-10-31T22:00:22',
         u'uuid': u'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
         u'workflow_id': u'03501d7626bd192f'}]
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_workflow_inputs`` command
-------------------------------

**Usage**::

    parsec workflows get_workflow_inputs [OPTIONS] WORKFLOW_ID LABEL

**Help**

Get a list of workflow input IDs that match the given label. If no input matches the given label, an empty list is returned.


**Output**


    list of workflow inputs matching the label query
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_workflows`` command
-------------------------

**Usage**::

    parsec workflows get_workflows [OPTIONS]

**Help**

Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.


**Output**


    A list of workflow dicts.
            For example::

              [{u'id': u'92c56938c2f9b315',
                u'name': u'Simple',
                u'url': u'/api/workflows/92c56938c2f9b315'}]
    
**Options**::


      --workflow_id TEXT  Encoded workflow ID (incompatible with ``name``)
      --name TEXT         Filter by name of workflow (incompatible with
                          ``workflow_id``). If multiple names match the given name,
                          all the workflows matching the argument will be returned.
      --published         if ``True``, return also published workflows
      -h, --help          Show this message and exit.
    

``import_shared_workflow`` command
----------------------------------

**Usage**::

    parsec workflows import_shared_workflow [OPTIONS] WORKFLOW_ID

**Help**

Imports a new workflow from the shared published workflows.


**Output**


    A description of the workflow.
     For example::

       {u'id': u'ee0e2b4b696d9092',
        u'model_class': u'StoredWorkflow',
        u'name': u'Super workflow that solves everything!',
        u'published': False,
        u'tags': [],
        u'url': u'/api/workflows/ee0e2b4b696d9092'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``import_workflow_dict`` command
--------------------------------

**Usage**::

    parsec workflows import_workflow_dict [OPTIONS] WORKFLOW_DICT

**Help**

Imports a new workflow given a dictionary representing a previously exported workflow.


**Output**


    
    
**Options**::


      --publish   if ``True`` the uploaded workflow will be published; otherwise it
                  will be visible only by the user which uploads it (default)
      -h, --help  Show this message and exit.
    

``import_workflow_from_local_path`` command
-------------------------------------------

**Usage**::

    parsec workflows import_workflow_from_local_path [OPTIONS]

**Help**

Imports a new workflow given the path to a file containing a previously exported workflow.


**Output**


    
    
**Options**::


      --publish   if ``True`` the uploaded workflow will be published; otherwise it
                  will be visible only by the user which uploads it (default)
      -h, --help  Show this message and exit.
    

``import_workflow_json`` command
--------------------------------

**Usage**::

    parsec workflows import_workflow_json [OPTIONS] WORKFLOW_JSON

**Help**

.. deprecated:: 0.9.0 Use :meth:`import_workflow_dict` instead.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``invoke_workflow`` command
---------------------------

**Usage**::

    parsec workflows invoke_workflow [OPTIONS] WORKFLOW_ID

**Help**

Invoke the workflow identified by ``workflow_id``. This will cause a workflow to be scheduled and return an object describing the workflow invocation.


**Output**


    A dict containing the workflow invocation describing the
     scheduling of the workflow. For example::

       {u'history_id': u'2f94e8ae9edff68a',
        u'id': u'df7a1f0c02a5b08e',
        u'inputs': {u'0': {u'id': u'a7db2fac67043c7e',
          u'src': u'hda',
          u'uuid': u'7932ffe0-2340-4952-8857-dbaa50f1f46a'}},
        u'model_class': u'WorkflowInvocation',
        u'state': u'ready',
        u'steps': [{u'action': None,
          u'id': u'd413a19dec13d11e',
          u'job_id': None,
          u'model_class': u'WorkflowInvocationStep',
          u'order_index': 0,
          u'state': None,
          u'update_time': u'2015-10-31T22:00:26',
          u'workflow_step_id': u'cbbbf59e8f08c98c',
          u'workflow_step_label': None,
          u'workflow_step_uuid': u'b81250fd-3278-4e6a-b269-56a1f01ef485'},
         {u'action': None,
          u'id': u'2f94e8ae9edff68a',
          u'job_id': u'e89067bb68bee7a0',
          u'model_class': u'WorkflowInvocationStep',
          u'order_index': 1,
          u'state': u'new',
          u'update_time': u'2015-10-31T22:00:26',
          u'workflow_step_id': u'964b37715ec9bd22',
          u'workflow_step_label': None,
          u'workflow_step_uuid': u'e62440b8-e911-408b-b124-e05435d3125e'}],
        u'update_time': u'2015-10-31T22:00:26',
        u'uuid': u'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
        u'workflow_id': u'03501d7626bd192f'}

   The ``params`` dict should be specified as follows::

     {STEP_ID: PARAM_DICT, ...}

   where PARAM_DICT is::

     {PARAM_NAME: VALUE, ...}

   For backwards compatibility, the following (deprecated) format is
   also supported for ``params``::

     {TOOL_ID: PARAM_DICT, ...}

   in which case PARAM_DICT affects all steps with the given tool id.
   If both by-tool-id and by-step-id specifications are used, the
   latter takes precedence.

   Finally (again, for backwards compatibility), PARAM_DICT can also
   be specified as::

     {'param': PARAM_NAME, 'value': VALUE}

   Note that this format allows only one parameter to be set per step.

   The ``replacement_params`` dict should map parameter names in
   post-job actions (PJAs) to their runtime values. For
   instance, if the final step has a PJA like the following::

     {u'RenameDatasetActionout_file1': {u'action_arguments': {u'newname': u'${output}'},
       u'action_type': u'RenameDatasetAction',
       u'output_name': u'out_file1'}}

   then the following renames the output dataset to 'foo'::

     replacement_params = {'output': 'foo'}

   see also `this email thread
   <http://lists.bx.psu.edu/pipermail/galaxy-dev/2011-September/006875.html>`_.

   .. warning::
     Historically, the ``run_workflow`` method consumed a ``dataset_map``
     data structure that was indexed by unencoded workflow step IDs. These
     IDs would not be stable across Galaxy instances. The new ``inputs``
     property is instead indexed by either the ``order_index`` property
     (which is stable across workflow imports) or the step UUID which is
     also stable.
    
**Options**::


      --inputs TEXT                   A mapping of workflow inputs to datasets and
                                      dataset collections. The datasets source can
                                      be a LibraryDatasetDatasetAssociation
                                      (``ldda``), LibraryDataset (``ld``),
                                      HistoryDatasetAssociation (``hda``), or
                                      HistoryDatasetCollectionAssociation
                                      (``hdca``).
      --params TEXT                   A mapping of non-datasets tool parameters (see
                                      below)
      --history_id TEXT               The encoded history ID where to store the
                                      workflow output. Alternatively,
                                      ``history_name`` may be specified to create a
                                      new history.
      --history_name TEXT             Create a new history with the given name to
                                      store the workflow output. If both
                                      ``history_id`` and ``history_name`` are
                                      provided, ``history_name`` is ignored. If
                                      neither is specified, a new 'Unnamed history'
                                      is created.
      --import_inputs_to_history      If ``True``, used workflow inputs will be
                                      imported into the history. If ``False``, only
                                      workflow outputs will be visible in the given
                                      history.
      --replacement_params TEXT       pattern-based replacements for post-job
                                      actions (see below)
      --allow_tool_state_corrections  If True, allow Galaxy to fill in missing tool
                                      state when running workflows. This may be
                                      useful for workflows using tools that have
                                      changed over time or for workflows built
                                      outside of Galaxy with only a subset of inputs
                                      defined.
      -h, --help                      Show this message and exit.
    

``run_invocation_step_action`` command
--------------------------------------

**Usage**::

    parsec workflows run_invocation_step_action [OPTIONS] WORKFLOW_ID

**Help**

nature of this action and what is expected will vary based on the the type of workflow step (the only currently valid action is True/False for pause steps).


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``run_workflow`` command
------------------------

**Usage**::

    parsec workflows run_workflow [OPTIONS] WORKFLOW_ID

**Help**

Run the workflow identified by ``workflow_id``.


**Output**


    A dict containing the history ID where the outputs are placed
     as well as output dataset IDs. For example::

       {u'history': u'64177123325c9cfd',
        u'outputs': [u'aa4d3084af404259']}

   The ``params`` dict should be specified as follows::

     {STEP_ID: PARAM_DICT, ...}

   where PARAM_DICT is::

     {PARAM_NAME: VALUE, ...}

   For backwards compatibility, the following (deprecated) format is
   also supported for ``params``::

     {TOOL_ID: PARAM_DICT, ...}

   in which case PARAM_DICT affects all steps with the given tool id.
   If both by-tool-id and by-step-id specifications are used, the
   latter takes precedence.

   Finally (again, for backwards compatibility), PARAM_DICT can also
   be specified as::

     {'param': PARAM_NAME, 'value': VALUE}

   Note that this format allows only one parameter to be set per step.

   The ``replacement_params`` dict should map parameter names in
   post-job actions (PJAs) to their runtime values. For
   instance, if the final step has a PJA like the following::

     {u'RenameDatasetActionout_file1': {u'action_arguments': {u'newname': u'${output}'},
       u'action_type': u'RenameDatasetAction',
       u'output_name': u'out_file1'}}

   then the following renames the output dataset to 'foo'::

     replacement_params = {'output': 'foo'}

   see also `this email thread
   <http://lists.bx.psu.edu/pipermail/galaxy-dev/2011-September/006875.html>`_.

   .. warning::
       This method waits for the whole workflow to be scheduled before
       returning and does not scale to large workflows as a result. This
       method has therefore been deprecated in favor of
       :meth:`invoke_workflow`, which also features improved default
       behavior for dataset input handling.
    
**Options**::


      --dataset_map TEXT          A mapping of workflow inputs to datasets. The
                                  datasets source can be a
                                  LibraryDatasetDatasetAssociation (``ldda``),
                                  LibraryDataset (``ld``), or
                                  HistoryDatasetAssociation (``hda``). The map must
                                  be in the following format: ``{'<input>': {'id':
                                  <encoded dataset ID>, 'src': '[ldda, ld, hda]'}}``
                                  (e.g. ``{'23': {'id': '29beef4fadeed09f', 'src':
                                  'ld'}}``)
      --params TEXT               A mapping of non-datasets tool parameters (see
                                  below)
      --history_id TEXT           The encoded history ID where to store the workflow
                                  output. Alternatively, ``history_name`` may be
                                  specified to create a new history.
      --history_name TEXT         Create a new history with the given name to store
                                  the workflow output. If both ``history_id`` and
                                  ``history_name`` are provided, ``history_name`` is
                                  ignored. If neither is specified, a new 'Unnamed
                                  history' is created.
      --import_inputs_to_history  If ``True``, used workflow inputs will be imported
                                  into the history. If ``False``, only workflow
                                  outputs will be visible in the given history.
      --replacement_params TEXT   pattern-based replacements for post-job actions
                                  (see below)
      -h, --help                  Show this message and exit.
    

``show_invocation`` command
---------------------------

**Usage**::

    parsec workflows show_invocation [OPTIONS] WORKFLOW_ID INVOCATION_ID

**Help**

Get a workflow invocation object representing the scheduling of a workflow. This object may be sparse at first (missing inputs and invocation steps) and will become more populated as the workflow is actually scheduled.


**Output**


    The workflow invocation.
     For example::

       {u'history_id': u'2f94e8ae9edff68a',
        u'id': u'df7a1f0c02a5b08e',
        u'inputs': {u'0': {u'id': u'a7db2fac67043c7e',
          u'src': u'hda',
          u'uuid': u'7932ffe0-2340-4952-8857-dbaa50f1f46a'}},
        u'model_class': u'WorkflowInvocation',
        u'state': u'ready',
        u'steps': [{u'action': None,
          u'id': u'd413a19dec13d11e',
          u'job_id': None,
          u'model_class': u'WorkflowInvocationStep',
          u'order_index': 0,
          u'state': None,
          u'update_time': u'2015-10-31T22:00:26',
          u'workflow_step_id': u'cbbbf59e8f08c98c',
          u'workflow_step_label': None,
          u'workflow_step_uuid': u'b81250fd-3278-4e6a-b269-56a1f01ef485'},
         {u'action': None,
          u'id': u'2f94e8ae9edff68a',
          u'job_id': u'e89067bb68bee7a0',
          u'model_class': u'WorkflowInvocationStep',
          u'order_index': 1,
          u'state': u'new',
          u'update_time': u'2015-10-31T22:00:26',
          u'workflow_step_id': u'964b37715ec9bd22',
          u'workflow_step_label': None,
          u'workflow_step_uuid': u'e62440b8-e911-408b-b124-e05435d3125e'}],
        u'update_time': u'2015-10-31T22:00:26',
        u'uuid': u'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
        u'workflow_id': u'03501d7626bd192f'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_invocation_step`` command
--------------------------------

**Usage**::

    parsec workflows show_invocation_step [OPTIONS] WORKFLOW_ID INVOCATION_ID

**Help**

See the details of a particular workflow invocation step.


**Output**


    The workflow invocation step.
     For example::

       {u'action': None,
        u'id': u'63cd3858d057a6d1',
        u'job_id': None,
        u'model_class': u'WorkflowInvocationStep',
        u'order_index': 2,
        u'state': None,
        u'update_time': u'2015-10-31T22:11:14',
        u'workflow_step_id': u'52e496b945151ee8',
        u'workflow_step_label': None,
        u'workflow_step_uuid': u'4060554c-1dd5-4287-9040-8b4f281cf9dc'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_workflow`` command
-------------------------

**Usage**::

    parsec workflows show_workflow [OPTIONS] WORKFLOW_ID

**Help**

Display information needed to run a workflow.


**Output**


    A description of the workflow and its inputs.
     For example::

       {u'id': u'92c56938c2f9b315',
        u'inputs': {u'23': {u'label': u'Input Dataset', u'value': u''}},
        u'name': u'Simple',
        u'url': u'/api/workflows/92c56938c2f9b315'}
    
**Options**::


      -h, --help  Show this message and exit.
    
