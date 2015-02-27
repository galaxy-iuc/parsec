import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception

@click.command('history_create')
@options.galaxy_instance()
@click.option(
    '--name',
    help="Name for the new history",
    default="Unnamed History",
)
@bioblend_exception
@pass_context
def cli(ctx, galaxy_instance, name, **kwds):
    """Create a new history and return the history ID
    """
    gi = get_galaxy_instance(galaxy_instance)
    result = gi.histories.create_history(name=name)
    # So much information that we're tossing away...
    print result['id']