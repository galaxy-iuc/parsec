import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('datatypes_get_sniffers')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """Displays a collection (list) of sniffers.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.datatypes.get_sniffers()

