
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('delete_history')
@options.galaxy_instance()


@click.option(
    "--history_id",
    help="Encoded history ID",
    type=str
)
@click.option(
    "--purge",
    help="Purge the history",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id=False, purge=False):
    """Delete a history.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.delete_history(history_id=history_id, purge=purge)
