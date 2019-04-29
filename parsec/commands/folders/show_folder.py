import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_folder')
@click.argument("folder_id", type=str)
@click.option(
    "--contents",
    help="True to get the contents of the folder, rather than just the folder details.",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, folder_id, contents=False):
    """Display information about a folder.

Output:

    dictionary including details of the folder
    """
    return ctx.gi.folders.show_folder(folder_id, contents=contents)
