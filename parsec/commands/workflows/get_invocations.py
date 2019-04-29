import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_invocations')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, workflow_id):
    """Get a list containing all the workflow invocations corresponding to the specified workflow.

Output:

    A list of workflow invocations.
          For example::

            [{u'history_id': u'2f94e8ae9edff68a',
              u'id': u'df7a1f0c02a5b08e',
              u'model_class': u'WorkflowInvocation',
              u'state': u'new',
              u'update_time': u'2015-10-31T22:00:22',
              u'uuid': u'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
              u'workflow_id': u'03501d7626bd192f'}]
    """
    return ctx.gi.workflows.get_invocations(workflow_id)
