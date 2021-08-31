import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_folder')
@click.argument("library_id", type=str, help="library id to inspect folders in")
@click.argument("folder_id", type=str, help="id of the folder to be inspected")
@pass_context
@custom_exception
@json_output
def cli(ctx, library_id, folder_id):
    """Get details about a given folder. The required ``folder_id`` can be obtained from the folder's library content details.

Output:

    Information about the folder
    """
    return ctx.gi.libraries.show_folder(library_id, folder_id)
