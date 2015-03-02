import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_upload_from_galaxy_filesystem')
@options.galaxy_instance()
@click.argument("filesystem_paths", type=str)
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
def cli(ctx, galaxy_instance, filesystem_paths, dbkey, roles, library_id="", folder_id="", file_type="", link_data_only=""):
    """Upload a set of files already present on the filesystem of the Galaxy server to a library.
    """
    return ctx.gi.libraries.upload_from_galaxy_filesystem(filesystem_paths, dbkey, roles, library_id=library_id, folder_id=folder_id, file_type=file_type, link_data_only=link_data_only)
