import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('upload_from_galaxy_filesystem')
@click.argument("library_id", type=str)
@click.argument("filesystem_paths", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--file_type",
    help="Galaxy file format name",
    default="auto",
    type=str
)
@click.option(
    "--dbkey",
    help="Dbkey",
    default="?",
    type=str
)
@click.option(
    "--link_data_only",
    help="either 'copy_files' (default) or 'link_to_files'. Setting to 'link_to_files' symlinks instead of copying the files",
    type=str
)
@click.option(
    "--roles",
    help="???",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, filesystem_paths, folder_id="", file_type="auto", dbkey="?", link_data_only="", roles=""):
    """Upload a set of files already present on the filesystem of the Galaxy server to a library.
    """
    return ctx.gi.libraries.upload_from_galaxy_filesystem(library_id, filesystem_paths, folder_id=folder_id, file_type=file_type, dbkey=dbkey, link_data_only=link_data_only, roles=roles)
