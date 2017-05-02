import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_matching_datasets')
@click.argument("history_id", type=str)

@click.option(
    "--name_filter",
    help="Only datasets whose name matches the ``name_filter`` regular expression will be returned; use plain strings for exact matches and None to match all datasets in the history",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, name_filter=""):
    """Get dataset details for matching datasets within a history.
    """
    return ctx.gi.histories.show_matching_datasets(history_id, name_filter=name_filter)
