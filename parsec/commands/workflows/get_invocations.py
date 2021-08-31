import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocations')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id):
    """Get a list containing all the workflow invocations corresponding to the specified workflow.

Output:

    A list of workflow invocations.
          For example::

            [{'history_id': '2f94e8ae9edff68a',
              'id': 'df7a1f0c02a5b08e',
              'model_class': 'WorkflowInvocation',
              'state': 'new',
              'update_time': '2015-10-31T22:00:22',
              'uuid': 'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
              'workflow_id': '03501d7626bd192f'}]
    """
    return ctx.gi.workflows.get_invocations(workflow_id)
