import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('upload_file_contents')
@click.argument("library_id", type=str)
@click.argument("pasted_content", type=str)
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
@click.option(
    "--tags",
    help="A list of tags to add to the datasets",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, library_id, pasted_content, folder_id="", file_type="auto", dbkey="?", tags=""):
    """Upload pasted_content to a data library as a new file.

Output:

    List with a single dictionary containing information about the LDDA
    """
    return ctx.gi.libraries.upload_file_contents(library_id, pasted_content, folder_id=folder_id, file_type=file_type, dbkey=dbkey, tags=tags)
