
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('export_history')
@options.galaxy_instance()


@click.option(
    "--history_id",
    help="history ID",
    type=str
)
@click.option(
    "--gzip",
    help="create .tar.gz archive if :obj:`True`, else .tar",
    type=bool
)
@click.option(
    "--include_hidden",
    help="whether to include hidden datasets in the export",
    type=bool
)
@click.option(
    "--include_deleted",
    help="whether to include deleted datasets in the export",
    type=bool
)
@click.option(
    "--wait",
    help="if :obj:`True`, block until the export is ready; else, return immediately",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id=False, gzip=True, include_hidden=False, include_deleted=False, wait=False):
    """Start a job to create an export archive for the given history.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.export_history(history_id=history_id, gzip=gzip, include_hidden=include_hidden, include_deleted=include_deleted, wait=wait)
