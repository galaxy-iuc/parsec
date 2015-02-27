import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('history_list')
@options.galaxy_instance()
@bioblend_exception
@click.option(
    '--deleted',
    is_flag=True,
    help='Show deleted histories',
)
@dict_output
@pass_context
def cli(ctx, galaxy_instance, deleted=False):
    """List histories available to a user
    """
    gi = get_galaxy_instance(galaxy_instance)
    return gi.histories.get_histories(deleted=deleted)
