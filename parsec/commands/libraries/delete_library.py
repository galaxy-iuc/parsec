import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('delete_library')
@click.argument("library_id", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id):
    """Delete a data library.

Output:

    
    """
    return ctx.gi.libraries.delete_library(library_id)
