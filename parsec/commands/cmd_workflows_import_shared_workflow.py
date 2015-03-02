import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_import_shared_workflow')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Imports a new workflow from the shared published workflows
    """
    return ctx.gi.workflows.import_shared_workflow()
