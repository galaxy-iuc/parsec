import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('datatypes_get_datatypes')
@options.galaxy_instance()


@click.option(
    "--extension_only",
    help="None"
)
@click.option(
    "--upload_only",
    help="None"
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, extension_only=False, upload_only=False):
    """Displays a collection (list) of datatypes.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.datatypes.get_datatypes(extension_only=extension_only, upload_only=upload_only)

