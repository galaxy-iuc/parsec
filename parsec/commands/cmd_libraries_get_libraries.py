import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_get_libraries')
@options.galaxy_instance()

@click.argument("name", type=str)
@click.argument("deleted", type=bool)

@click.option(
    "--library_id",
    help="filter for library by library id",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, name, deleted, library_id=False):
    """Get all the libraries or filter for specific one(s) via the provided name or ID. Provide only one argument: ``name`` or ``library_id``, but not both.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.get_libraries(name, deleted, library_id=library_id)

