import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('get_status')
@click.argument("history_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id):
    """Returns the state of this history

Output:

    A dict documenting the current state of the history. Has the following keys:
            'state' = This is the current state of the history, such as ok, error, new etc.
            'state_details' = Contains individual statistics for various dataset states.
            'percent_complete' = The overall number of datasets processed to completion.
    """
    return ctx.gi.histories.get_status(history_id)
