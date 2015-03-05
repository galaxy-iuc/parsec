import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('datatypes_get_sniffers')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Displays a collection (list) of sniffers.
    """
    return ctx.gi.datatypes.get_sniffers()
