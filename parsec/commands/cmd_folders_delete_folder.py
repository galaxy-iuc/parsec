import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('folders_delete_folder')
@options.galaxy_instance()

@click.option(
    "--folder_id",
    help="the folder's encoded id, prefixed by 'F'",
    type=str
)
@click.option(
    "--undelete",
    help="If set to True, the folder will be undeleted (i.e. the `deleted` mark will be removed)",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, folder_id=False, undelete=False):
    """Marks the folder with the given ``id`` as `deleted` (or removes the `deleted` mark if the `undelete` param is True).
    """
    return ctx.gi.folders.delete_folder(folder_id=folder_id, undelete=undelete)
