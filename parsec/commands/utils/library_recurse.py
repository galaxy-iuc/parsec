
import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output, _arg_split

@click.command('library_recurse')
@click.argument("library_id")
@click.option(
    "--path",
    help="Folder path to filter on (otherwise root of repo)",
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, library_id, path=""):
    """Get all the folders or filter specific one(s) via the provided ``name`` or ``folder_id`` in data library with id ``library_id``. Provide only one argument: ``name`` or ``folder_id``, but not both.

Output:

     list of dicts each containing basic information about a folder

    """

    stuff = [
        thing for thing in
        ctx.gi.libraries.show_library(library_id, contents=True)
        if not path or thing['name'][0:len(path)] == path
    ]
    return stuff
