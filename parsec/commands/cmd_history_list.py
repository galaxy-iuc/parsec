import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance

HIST_HEADERS = ['id', 'name', 'published', 'deleted', 'tags', 'url']
HIST_TEMPLATE = '\t'.join(["%%(%s)s" % col for col in HIST_HEADERS])

@click.command('history_list')
@options.galaxy_instance()
@pass_context
def cli(ctx, galaxy_instance, **kwds):
    """List histories available to a user
    """
    gi = get_galaxy_instance(galaxy_instance)

    print '# ' + '\t'.join(HIST_HEADERS)
    for hist in gi.histories.get_histories():
        print HIST_TEMPLATE % hist
