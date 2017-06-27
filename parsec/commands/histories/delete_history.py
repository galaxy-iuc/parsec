import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('delete_history')
@click.argument("history_id", type=str)

@click.option(
    "--purge",
    help="if ``True``, also purge (permanently delete) the history",
    is_flag=True
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, purge=False):
    """Delete a history.

Output:

    
    """
    return ctx.gi.histories.delete_history(history_id, purge=purge)
