import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_invocation_step')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@click.argument("step_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id, invocation_id, step_id):
    """See the details of a particular workflow invocation step.

Output:

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
    """
    return ctx.gi.workflows.show_invocation_step(workflow_id, invocation_id, step_id)
