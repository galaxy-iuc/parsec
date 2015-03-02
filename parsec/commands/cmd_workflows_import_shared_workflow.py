import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_import_shared_workflow')
@options.galaxy_instance()

@click.argument("workflow_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, workflow_id):
    """Imports a new workflow from the shared published workflows
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.import_shared_workflow(workflow_id)

