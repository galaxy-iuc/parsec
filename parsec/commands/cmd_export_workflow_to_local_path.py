import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows.export_workflow_to_local_path')
@options.galaxy_instance()

@click.argument("use_default_filename", type=bool)

@click.option(
    "--workflow_id",
    help="Encoded workflow ID",
    type=str
)
@click.option(
    "--file_local_path",
    help="Local path to which the exported file will be saved. (Should not contain filename if use_default_name=True)",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, use_default_filename, workflow_id=True, file_local_path=True):
    """Exports a workflow to a given local path.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.export_workflow_to_local_path(use_default_filename, workflow_id=workflow_id, file_local_path=file_local_path)

