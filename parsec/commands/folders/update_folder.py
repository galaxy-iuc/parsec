import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('update_folder')
@click.argument("folder_id", type=str)
@click.argument("name", type=str)
@click.option(
    "--description",
    help="folder's description",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, folder_id, name, description=""):
    """Update folder information.

Output:

    details of the updated folder
    """
    return ctx.gi.folders.update_folder(folder_id, name, description=description)
