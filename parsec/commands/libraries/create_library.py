import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_library')
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
    """Create a data library with the properties defined in the arguments.
    """
    return ctx.gi.libraries.create_library(name, description=description, synopsis=synopsis)
