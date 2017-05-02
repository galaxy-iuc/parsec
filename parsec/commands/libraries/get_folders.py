import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_folders')
@click.argument("library_id")

@click.option(
    "--folder_id",
    help="filter for folder by folder id",
    type=str
)
@click.option(
    "--name",
    help="filter for folder by name. For ``name`` specify the full path of the folder starting from the library's root folder, e.g. ``/subfolder/subsubfolder``.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, folder_id="", name=""):
    """Get all the folders or filter specific one(s) via the provided ``name`` or ``folder_id`` in data library with id ``library_id``. Provide only one argument: ``name`` or ``folder_id``, but not both.
    """
    return ctx.gi.libraries.get_folders(library_id, folder_id=folder_id, name=name)
