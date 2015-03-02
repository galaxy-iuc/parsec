import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_delete_library_dataset')
@options.galaxy_instance()
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--purged",
    help="Indicate that the dataset should be purged (permanently deleted)",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, dataset_id, purged=False):
    """Delete a library dataset in a data library.
    """
    return ctx.gi.libraries.delete_library_dataset(library_id, dataset_id, purged=purged)