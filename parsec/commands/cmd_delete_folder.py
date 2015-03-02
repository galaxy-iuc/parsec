import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('folders.delete_folder')
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
    gi = get_galaxy_instance(galaxy_instance)

    return gi.folders.delete_folder(folder_id=folder_id, undelete=undelete)

