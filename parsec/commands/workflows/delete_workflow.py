import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('delete_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, workflow_id):
    """Delete a workflow identified by `workflow_id`.

Output:

    A message about the deletion

        .. warning::
            Deleting a workflow is irreversible - all workflow data
            will be permanently deleted.
    """
    return ctx.gi.workflows.delete_workflow(workflow_id)
