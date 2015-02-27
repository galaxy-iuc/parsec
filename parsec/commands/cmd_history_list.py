import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception

HIST_HEADERS = ['id', 'name', 'published', 'deleted', 'tags', 'url']
HIST_TEMPLATE = '\t'.join(["%%(%s)s" % col for col in HIST_HEADERS])

@click.command('history_list')
@options.galaxy_instance()
@bioblend_exception
@click.option(
    '--deleted',
    is_flag=True,
    help='Show deleted histories',
)
@pass_context
def cli(ctx, galaxy_instance, deleted=False):
    """List histories available to a user
    """
    gi = get_galaxy_instance(galaxy_instance)

    print '# ' + '\t'.join(HIST_HEADERS)
    for hist in gi.histories.get_histories(deleted=deleted):
        print HIST_TEMPLATE % hist
