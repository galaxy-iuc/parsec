import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('delete_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id):
    """Delete a workflow identified by `workflow_id`.

Output:

    
    """
    return ctx.gi.workflows.delete_workflow(workflow_id)
