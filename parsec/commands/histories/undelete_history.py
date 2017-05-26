import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('undelete_history')
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id):
    """Undelete a history
    """
    return ctx.gi.histories.undelete_history(history_id)
