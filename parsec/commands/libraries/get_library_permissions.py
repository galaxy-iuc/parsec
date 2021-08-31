import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_library_permissions')
@click.argument("library_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, library_id):
    """Get the permissions for a library.

Output:

    dictionary with all applicable permissions' values
    """
    return ctx.gi.libraries.get_library_permissions(library_id)
