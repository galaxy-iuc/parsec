import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_folder')
@click.argument("folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, folder_id):
    """Display information about a folder.
    """
    return ctx.gi.folders.show_folder(folder_id)
