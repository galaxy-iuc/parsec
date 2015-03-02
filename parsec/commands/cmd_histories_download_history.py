import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_download_history')
@options.galaxy_instance()

@click.argument("outf", type=click.File('rb+'))
@click.argument("chunk_size", type=int)

@click.option(
    "--history_id",
    help="history ID",
    type=str
)
@click.option(
    "--jeha_id",
    help="jeha ID (this should be obtained via :meth:`export_history`)",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, outf, chunk_size, history_id=4096, jeha_id=4096):
    """Download a history export archive.  Use :meth:`export_history` to create an export.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.download_history(outf, chunk_size, history_id=history_id, jeha_id=jeha_id)

