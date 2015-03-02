import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_delete_workflow')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Delete a workflow identified by `workflow_id`.
    """
    return ctx.gi.workflows.delete_workflow()
