import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_show_workflow')
@options.galaxy_instance()
@click.argument("workflow_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, workflow_id):
    """Display information needed to run a workflow
    """
    return ctx.gi.workflows.show_workflow(workflow_id)
