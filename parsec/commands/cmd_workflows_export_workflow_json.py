import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_export_workflow_json')
@options.galaxy_instance()
@click.argument("workflow_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, workflow_id):
    """Exports a workflow
    """
    return ctx.gi.workflows.export_workflow_json(workflow_id)
