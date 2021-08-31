import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_invocation_step')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@click.argument("step_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, invocation_id, step_id):
    """See the details of a particular workflow invocation step.

Output:

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
    """
    return ctx.gi.workflows.show_invocation_step(workflow_id, invocation_id, step_id)
