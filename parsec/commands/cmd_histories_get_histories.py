import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_get_histories')
@options.galaxy_instance()

@click.argument("name", type=str)
@click.argument("deleted")

@click.option(
    "--history_id",
    help="Encoded history ID to filter on",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, name, deleted, history_id=False):
    """Get all histories or filter the specific one(s) via the provided ``name`` or ``history_id``. Provide only one argument, ``name`` or ``history_id``, but not both.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.get_histories(name, deleted, history_id=history_id)

