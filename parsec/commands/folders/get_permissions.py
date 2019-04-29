import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('get_permissions')
@click.argument("folder_id", type=str)
@click.argument("scope", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, folder_id, scope):
    """Get the permissions of a folder.

Output:

    dictionary including details of the folder
    """
    return ctx.gi.folders.get_permissions(folder_id, scope)
