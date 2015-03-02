import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_upload_file_from_url')
@options.galaxy_instance()

@click.argument("file_url", type=str)
@click.argument("dbkey", type=str)

@click.option(
    "--library_id",
    help="id of the library where to place the uploaded file. If not provided, the root library will be used",
    type=str
)
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

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, file_url, dbkey, library_id="", folder_id="", file_type=""):
    """Upload a file to a library from a URL.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.upload_file_from_url(file_url, dbkey, library_id=library_id, folder_id=folder_id, file_type=file_type)

