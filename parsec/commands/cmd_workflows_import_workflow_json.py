import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_import_workflow_json')
@options.galaxy_instance()

@click.argument("workflow_json", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, workflow_json):
    """Imports a new workflow given a json representation of a previously exported workflow.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.import_workflow_json(workflow_json)

