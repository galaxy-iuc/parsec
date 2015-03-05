import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('workflows_import_shared_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id):
    """Imports a new workflow from the shared published workflows
    """
    return ctx.gi.workflows.import_shared_workflow(workflow_id)
