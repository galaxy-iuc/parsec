import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('undelete_history')
@click.argument("history_id", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id):
    """Undelete a history

Output:

    
    """
    return ctx.gi.histories.undelete_history(history_id)
