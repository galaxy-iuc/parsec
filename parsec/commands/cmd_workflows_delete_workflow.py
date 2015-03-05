import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('workflows_delete_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id):
    """Delete a workflow identified by `workflow_id`.
    """
    return ctx.gi.workflows.delete_workflow(workflow_id)
