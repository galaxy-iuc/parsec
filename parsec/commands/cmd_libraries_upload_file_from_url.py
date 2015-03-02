import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_upload_file_from_url')
@options.galaxy_instance()
@click.argument("library_id", type=str)
@click.argument("file_url", type=str)

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
def cli(ctx, galaxy_instance, library_id, file_url, folder_id="", file_type="", dbkey=""):
    """Upload a file to a library from a URL.
    """
    return ctx.gi.libraries.upload_file_from_url(library_id, file_url, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
