import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_matching_datasets')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("name_filter", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, name_filter):
    """Get dataset details for matching datasets within a history.
    """
    return ctx.gi.histories.show_matching_datasets(history_id, name_filter)
