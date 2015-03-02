
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_folder')
@options.galaxy_instance()

@click.argument("library_id", type=str)
@click.argument("folder_name", type=str)
@click.argument("description", type=str)
@click.argument("base_folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, library_id, folder_name, description, base_folder_id):
    """Create a folder in a library.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.create_folder(library_id, folder_name, description, base_folder_id)
