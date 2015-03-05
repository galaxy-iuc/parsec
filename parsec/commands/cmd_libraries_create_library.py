import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('libraries_create_library')
@click.argument("name", type=str)
@click.option(
    "--description",
    help="Optional data library description",
    type=str
)
@click.option(
    "--synopsis",
    help="Optional data library synopsis",
    type=str
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, name, description="", synopsis=""):
    """Create a data library with the properties defined in the arguments. Return a list of JSON dicts, looking like so::
    """
    return ctx.gi.libraries.create_library(
        name,
        description=description,
        synopsis=synopsis)
