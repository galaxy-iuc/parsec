import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_invocation')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, invocation_id):
    """Get a workflow invocation object representing the scheduling of a workflow. This object may be sparse at first (missing inputs and invocation steps) and will become more populated as the workflow is actually scheduled.

Output:

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
    """
    return ctx.gi.workflows.show_invocation(workflow_id, invocation_id)
