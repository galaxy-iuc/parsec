import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_upload_file_from_server')
@options.galaxy_instance()

@click.argument("server_dir", type=str)
@click.argument("dbkey", type=str)
@click.argument("roles", type=str)

@click.option(
    "--library_id",
    help="id of the library where to place the uploaded file. If not provided, the root library will be used",
    type=str
)
@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    type=str
)
@click.option(
    "--link_data_only",
    help="either 'copy_files' (default) or 'link_to_files'. Setting to 'link_to_files' symlinks instead of copying the files",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, server_dir, dbkey, roles, library_id="", folder_id="", file_type="", link_data_only=""):
    """Upload all files in the specified subdirectory of the Galaxy library import directory to a library.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.upload_file_from_server(server_dir, dbkey, roles, library_id=library_id, folder_id=folder_id, file_type=file_type, link_data_only=link_data_only)

