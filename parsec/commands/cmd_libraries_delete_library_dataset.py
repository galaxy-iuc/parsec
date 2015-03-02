import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_delete_library_dataset')
@options.galaxy_instance()
@click.argument("purged", type=bool)

@click.option(
    "--library_id",
    help="library id where dataset is found in",
    type=str
)
@click.option(
    "--dataset_id",
    help="id of the dataset to be deleted",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, purged, library_id=False, dataset_id=False):
    """Delete a library dataset in a data library.
    """
    return ctx.gi.libraries.delete_library_dataset(purged, library_id=library_id, dataset_id=dataset_id)
