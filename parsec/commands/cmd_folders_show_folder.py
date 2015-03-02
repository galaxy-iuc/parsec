import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('folders_show_folder')
@options.galaxy_instance()
@click.argument("folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, folder_id):
    """Display information about a folder.
    """
    return ctx.gi.folders.show_folder(folder_id)
