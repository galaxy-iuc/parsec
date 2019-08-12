import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('delete_library')
@click.argument("library_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id):
    """Delete a data library.

Output:

    Information about the deleted library

        .. warning::
          Deleting a data library is irreversible - all of the data from the
          library will be permanently deleted.
    """
    return ctx.gi.libraries.delete_library(library_id)
