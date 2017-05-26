import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('download_history')
@click.argument("history_id", type=str)
@click.argument("jeha_id", type=str)
@click.argument("outf", type=click.File('rb+'))

@click.option(
    "--chunk_size",
    help="how many bytes at a time should be read into memory",
    default="4096",
    type=int
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, jeha_id, outf, chunk_size=4096):
    """Download a history export archive.  Use :meth:`export_history` to create an export.
    """
    return ctx.gi.histories.download_history(history_id, jeha_id, outf, chunk_size=chunk_size)
