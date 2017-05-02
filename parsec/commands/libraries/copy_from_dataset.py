import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('copy_from_dataset')
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--message",
    help="message for copying action",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, dataset_id, folder_id="", message=""):
    """Copy a Galaxy dataset into a library.
    """
    return ctx.gi.libraries.copy_from_dataset(library_id, dataset_id, folder_id=folder_id, message=message)
