
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('upload_file_from_local_path')
@options.galaxy_instance()

@click.argument("file_local_path", type=str)
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

def cli(ctx, galaxy_instance, file_local_path, dbkey, library_id="", folder_id="", file_type=""):
    """Read local file contents from file_local_path and upload data to a library.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.upload_file_from_local_path(file_local_path, dbkey, library_id=library_id, folder_id=folder_id, file_type=file_type)
