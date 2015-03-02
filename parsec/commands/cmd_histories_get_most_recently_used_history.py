import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_get_most_recently_used_history')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """Returns the current user's most recently used history (not deleted).
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.get_most_recently_used_history()

