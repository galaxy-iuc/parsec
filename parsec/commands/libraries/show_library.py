import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_library')
@click.argument("library_id", type=str)

@click.option(
    "--contents",
    help="True if want to get contents of the library (rather than just the library details)",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, contents=False):
    """Get information about a library.
    """
    return ctx.gi.libraries.show_library(library_id, contents=contents)
