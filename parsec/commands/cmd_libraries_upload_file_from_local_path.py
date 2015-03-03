import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_upload_file_from_local_path')
@options.galaxy_instance()
@click.argument("library_id", type=str)
@click.argument("file_local_path", type=str)

@click.option(
    "--folder_id",
    help="id of the folder to download into",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    type=str
)
@click.option(
    "--dbkey",
    help="Dbkey",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, file_local_path, folder_id="", file_type="", dbkey=""):
    """Read local file contents from file_local_path and upload data to a library.
    """
    return ctx.gi.libraries.upload_file_from_local_path(library_id, file_local_path, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
