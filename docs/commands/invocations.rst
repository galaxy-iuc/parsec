invocations
===========

This section is auto-generated from the help text for the parsec command
``invocations``.


``cancel_invocation`` command
-----------------------------

**Usage**::

    parsec invocations cancel_invocation [OPTIONS] INVOCATION_ID

**Help**

Cancel the scheduling of a workflow.


**Output**


    The workflow invocation being cancelled
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_invocation_biocompute_object`` command
--------------------------------------------

**Usage**::

    parsec invocations get_invocation_biocompute_object [OPTIONS]

**Help**

Get a BioCompute object for an invocation.


**Output**


    The BioCompute object
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_invocation_report`` command
---------------------------------

**Usage**::

    parsec invocations get_invocation_report [OPTIONS] INVOCATION_ID

**Help**

Get a Markdown report for an invocation.


**Output**


    The invocation report.
     For example::

       {'markdown': '
# Workflow Execution Summary of Example workflow


        ## Workflow Inputs


## Workflow Outputs



        ## Workflow
```galaxy

        workflow_display(workflow_id=f2db41e1fa331b3e)
```
',
        'render_format': 'markdown',
        'workflows': {'f2db41e1fa331b3e': {'name': 'Example workflow'}}}
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_invocation_report_pdf`` command
-------------------------------------

**Usage**::

    parsec invocations get_invocation_report_pdf [OPTIONS] INVOCATION_ID

**Help**

Get a PDF report for an invocation.


**Output**


    
    
**Options**::


      --chunk_size INTEGER  Size of chunks to requests, defaults to
                            bioblend.CHUNK_SIZE  [default: 4096]
    
      -h, --help            Show this message and exit.
    

``get_invocation_step_jobs_summary`` command
--------------------------------------------

**Usage**::

    parsec invocations get_invocation_step_jobs_summary [OPTIONS]

**Help**

Get a detailed summary of an invocation, listing all jobs with their job IDs and current states.


**Output**


    The invocation step jobs summary.
     For example::

       [{'id': 'e85a3be143d5905b',
         'model': 'Job',
         'populated_state': 'ok',
         'states': {'ok': 1}},
        {'id': 'c9468fdb6dc5c5f1',
         'model': 'Job',
         'populated_state': 'ok',
         'states': {'running': 1}},
        {'id': '2a56795cad3c7db3',
         'model': 'Job',
         'populated_state': 'ok',
         'states': {'new': 1}}]
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_invocation_summary`` command
----------------------------------

**Usage**::

    parsec invocations get_invocation_summary [OPTIONS] INVOCATION_ID

**Help**

Get a summary of an invocation, stating the number of jobs which succeed, which are paused and which have errored.


**Output**


    The invocation summary.
     For example::

       {'states': {'paused': 4, 'error': 2, 'ok': 2},
        'model': 'WorkflowInvocation',
        'id': 'a799d38679e985db',
        'populated_state': 'ok'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_invocations`` command
---------------------------

**Usage**::

    parsec invocations get_invocations [OPTIONS]

**Help**

Get all workflow invocations, or select a subset by specifying optional arguments for filtering (e.g. a workflow ID).


**Output**


    A list of workflow invocations.
     For example::

       [{'history_id': '2f94e8ae9edff68a',
         'id': 'df7a1f0c02a5b08e',
         'model_class': 'WorkflowInvocation',
         'state': 'new',
         'update_time': '2015-10-31T22:00:22',
         'uuid': 'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
         'workflow_id': '03501d7626bd192f'}]
    
**Options**::


      --workflow_id TEXT  Encoded workflow ID to filter on
      --history_id TEXT   Encoded history ID to filter on
      --user_id TEXT      Encoded user ID to filter on. This must be your own user
                          ID if your are not an admin user.
    
      --include_terminal  Whether to include terminal states.  [default: True]
      --limit INTEGER     Maximum number of invocations to return - if specified,
                          the most recent invocations will be returned.
    
      --view TEXT         Level of detail to return per invocation, either 'element'
                          or 'collection'.  [default: collection]
    
      --step_details      If 'view' is 'element', also include details on individual
                          steps.
    
      -h, --help          Show this message and exit.
    

``rerun_invocation`` command
----------------------------

**Usage**::

    parsec invocations rerun_invocation [OPTIONS] INVOCATION_ID

**Help**

Rerun a workflow invocation. For more extensive documentation of all parameters, see the ``gi.workflows.invoke_workflow()`` method.


**Output**


    A dict describing the new workflow invocation.

   .. note::
     This method can only be used with Galaxy ``release_21.01`` or later.
    
**Options**::


      --inputs_update TEXT            If different datasets should be used to the
                                      original invocation, this should contain a
                                      mapping of workflow inputs to the new datasets
                                      and dataset collections.
    
      --params_update TEXT            If different non-dataset tool parameters
                                      should be used to the original invocation,
                                      this should contain a mapping of the new
                                      parameter values.
    
      --history_id TEXT               The encoded history ID where to store the
                                      workflow outputs. Alternatively,
                                      ``history_name`` may be specified to create a
                                      new history.
    
      --history_name TEXT             Create a new history with the given name to
                                      store the workflow outputs. If both
                                      ``history_id`` and ``history_name`` are
                                      provided, ``history_name`` is ignored. If
                                      neither is specified, a new 'Unnamed history'
                                      is created.
    
      --import_inputs_to_history      If ``True``, used workflow inputs will be
                                      imported into the history. If ``False``, only
                                      workflow outputs will be visible in the given
                                      history.
    
      --replacement_params TEXT       pattern-based replacements for post-job
                                      actions
    
      --allow_tool_state_corrections  If True, allow Galaxy to fill in missing tool
                                      state when running workflows. This may be
                                      useful for workflows using tools that have
                                      changed over time or for workflows built
                                      outside of Galaxy with only a subset of inputs
                                      defined.
    
      --inputs_by TEXT                Determines how inputs are referenced. Can be
                                      "step_index|step_uuid" (default),
                                      "step_index", "step_id", "step_uuid", or
                                      "name".
    
      --parameters_normalized         Whether Galaxy should normalize the input
                                      parameters to ensure everything is referenced
                                      by a numeric step ID. Default is ``False``,
                                      but when setting parameters for a subworkflow,
                                      ``True`` is required.
    
      -h, --help                      Show this message and exit.
    

``run_invocation_step_action`` command
--------------------------------------

**Usage**::

    parsec invocations run_invocation_step_action [OPTIONS] INVOCATION_ID

**Help**

nature of this action and what is expected will vary based on the the type of workflow step (the only currently valid action is True/False for pause steps).


**Output**


    Representation of the workflow invocation step
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_invocation`` command
---------------------------

**Usage**::

    parsec invocations show_invocation [OPTIONS] INVOCATION_ID

**Help**

Get a workflow invocation dictionary representing the scheduling of a workflow. This dictionary may be sparse at first (missing inputs and invocation steps) and will become more populated as the workflow is actually scheduled.


**Output**


    The workflow invocation.
     For example::

       {'history_id': '2f94e8ae9edff68a',
        'id': 'df7a1f0c02a5b08e',
        'inputs': {'0': {'id': 'a7db2fac67043c7e',
          'src': 'hda',
          'uuid': '7932ffe0-2340-4952-8857-dbaa50f1f46a'}},
        'model_class': 'WorkflowInvocation',
        'state': 'ready',
        'steps': [{'action': None,
          'id': 'd413a19dec13d11e',
          'job_id': None,
          'model_class': 'WorkflowInvocationStep',
          'order_index': 0,
          'state': None,
          'update_time': '2015-10-31T22:00:26',
          'workflow_step_id': 'cbbbf59e8f08c98c',
          'workflow_step_label': None,
          'workflow_step_uuid': 'b81250fd-3278-4e6a-b269-56a1f01ef485'},
         {'action': None,
          'id': '2f94e8ae9edff68a',
          'job_id': 'e89067bb68bee7a0',
          'model_class': 'WorkflowInvocationStep',
          'order_index': 1,
          'state': 'new',
          'update_time': '2015-10-31T22:00:26',
          'workflow_step_id': '964b37715ec9bd22',
          'workflow_step_label': None,
          'workflow_step_uuid': 'e62440b8-e911-408b-b124-e05435d3125e'}],
        'update_time': '2015-10-31T22:00:26',
        'uuid': 'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
        'workflow_id': '03501d7626bd192f'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_invocation_step`` command
--------------------------------

**Usage**::

    parsec invocations show_invocation_step [OPTIONS] INVOCATION_ID STEP_ID

**Help**

See the details of a particular workflow invocation step.


**Output**


    The workflow invocation step.
     For example::

       {'action': None,
        'id': '63cd3858d057a6d1',
        'job_id': None,
        'model_class': 'WorkflowInvocationStep',
        'order_index': 2,
        'state': None,
        'update_time': '2015-10-31T22:11:14',
        'workflow_step_id': '52e496b945151ee8',
        'workflow_step_label': None,
        'workflow_step_uuid': '4060554c-1dd5-4287-9040-8b4f281cf9dc'}
    
**Options**::


      -h, --help  Show this message and exit.
    

``wait_for_invocation`` command
-------------------------------

**Usage**::

    parsec invocations wait_for_invocation [OPTIONS] INVOCATION_ID

**Help**

Wait until an invocation is in a terminal state.


**Output**


    Details of the workflow invocation.
    
**Options**::


      --maxwait FLOAT   Total time (in seconds) to wait for the invocation state to
                        become terminal. If the invocation state is not terminal
                        within this time, a ``TimeoutException`` will be raised.
                        [default: 12000]
    
      --interval FLOAT  Time (in seconds) to wait between 2 consecutive checks.
                        [default: 3]
    
      --check           Whether to check if the invocation terminal state is
                        'scheduled'.  [default: True]
    
      -h, --help        Show this message and exit.
    
