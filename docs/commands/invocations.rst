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

Get a list containing all workflow invocations.


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


      -h, --help  Show this message and exit.
    

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
    
