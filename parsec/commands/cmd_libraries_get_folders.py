import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_get_folders')
@options.galaxy_instance()

@click.argument("folder_id", type=str)
@click.argument("name", type=str)

@click.option(
    "--library_id",
    help="None"
)
@click.option(
    "--deleted",
    help="If set to ``True``, return folders that have been deleted.",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, folder_id, name, library_id=False, deleted=False):
    """Get all the folders or filter specific one(s) via the provided ``name`` or ``folder_id`` in data library with id ``library_id``. Provide only one argument: ``name`` or ``folder_id``, but not both.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.get_folders(folder_id, name, library_id=library_id, deleted=deleted)

