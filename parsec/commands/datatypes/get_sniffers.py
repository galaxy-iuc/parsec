import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_sniffers')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of all installed sniffers.
    """
    return ctx.gi.datatypes.get_sniffers()
