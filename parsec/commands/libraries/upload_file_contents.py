import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

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

@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, pasted_content, folder_id="", file_type="auto", dbkey="?"):
    """Upload pasted_content to a data library as a new file.

Output:

    
    """
    return ctx.gi.libraries.upload_file_contents(library_id, pasted_content, folder_id=folder_id, file_type=file_type, dbkey=dbkey)
