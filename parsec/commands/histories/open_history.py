import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('open_history')
@click.argument("history_id", type=str)
@pass_context
@custom_exception
@text_output
def cli(ctx, history_id):
    """Open Galaxy in a new tab of the default web browser and switch to the specified history.

Output:

    ``None``

        .. warning::
          After opening the specified history, all previously opened Galaxy tabs
          in the browser session will have the current history changed to this
          one, even if the interface still shows another history. Refreshing
          any such tab is recommended.
    """
    return ctx.gi.histories.open_history(history_id)
