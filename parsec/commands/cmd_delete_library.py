
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('delete_library')
@options.galaxy_instance()

@click.argument("library_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, library_id):
    """Delete a data library
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.delete_library(library_id)
