import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception

@click.command('history_create')
@options.galaxy_instance()

@click.argument('id')
@click.option(
    '--purge',
    help='Purge a history',
    is_flag=True,
)
@pass_context
@bioblend_exception
def cli(ctx, galaxy_instance, id, purge=False, **kwds):
    """Delete a history by ID
    """
    gi = get_galaxy_instance(galaxy_instance)
    print(gi.histories.delete_history(id, purge=purge))
