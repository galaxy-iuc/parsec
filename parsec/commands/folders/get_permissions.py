import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_permissions')
@click.argument("folder_id", type=str, help="the folder's encoded id, prefixed by 'F'")
@click.argument("scope", type=str, help="scope of permissions, either 'current' or 'available'")
@pass_context
@custom_exception
@json_output
def cli(ctx, folder_id, scope):
    """Get the permissions of a folder.

Output:

    dictionary including details of the folder
    """
    return ctx.gi.folders.get_permissions(folder_id, scope)
