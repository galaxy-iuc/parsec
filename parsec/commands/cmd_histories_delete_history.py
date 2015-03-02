import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_delete_history')
@options.galaxy_instance()
@click.argument("history_id", type=str)

@click.option(
    "--purge",
    help="Purge the history",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, purge=False):
    """Delete a history.
    """
    return ctx.gi.histories.delete_history(history_id, purge=purge)
