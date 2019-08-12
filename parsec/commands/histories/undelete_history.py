import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('undelete_history')
@click.argument("history_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, history_id):
    """Undelete a history

Output:

    'OK' if it was deleted
    """
    return ctx.gi.histories.undelete_history(history_id)
