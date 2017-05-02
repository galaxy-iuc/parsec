import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('update_history')
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    return ctx.gi.histories.update_history(history_id)