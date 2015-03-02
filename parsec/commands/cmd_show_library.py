
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_library')
@options.galaxy_instance()


@click.option(
    "--library_id",
    help="filter for library by library id",
    type=str
)
@click.option(
    "--contents",
    help="True if want to get contents of the library (rather than just the library details).",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, library_id=False, contents=False):
    """Get information about a library.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.show_library(library_id=library_id, contents=contents)
