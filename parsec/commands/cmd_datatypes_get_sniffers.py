import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('datatypes_get_sniffers')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Displays a collection (list) of sniffers.
    """
    return ctx.gi.datatypes.get_sniffers()
