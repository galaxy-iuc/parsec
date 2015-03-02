import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_history')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("deleted", type=str)
@click.argument("visible", type=str)
@click.argument("details", type=str)
@click.argument("types", type=str)

@click.option(
    "--contents",
    help="When true, the complete list of datasets in the given history.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, deleted, visible, details, types, contents=False):
    """Get details of a given history. By default, just get the history meta information.
    """
    return ctx.gi.histories.show_history(history_id, deleted, visible, details, types, contents=contents)
