import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('upload_file_from_local_path')
@click.argument("library_id", type=str)
@click.argument("file_local_path", type=str)
@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded file. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    default="auto",
    show_default=True,
    type=str
)
@click.option(
    "--dbkey",
    help="Dbkey",
    default="?",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, library_id, file_local_path, folder_id="", file_type="auto", dbkey="?"):
    """Read local file contents from file_local_path and upload data to a library.

Output:

    List with a single dictionary containing information about the LDDA
    """
    return ctx.gi.libraries.upload_file_from_local_path(library_id, file_local_path, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
