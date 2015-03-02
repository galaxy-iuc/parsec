import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('folders_show_folder')
@options.galaxy_instance()

@click.argument("folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, folder_id):
    """Display information about a folder.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.folders.show_folder(folder_id)

