import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_library')
@click.argument("library_id", type=str)
@click.option(
    "--contents",
    help="whether to get contents of the library (rather than just the library details)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, contents=False):
    """Get information about a library.

Output:

    details of the given library
    """
    return ctx.gi.libraries.show_library(library_id, contents=contents)
