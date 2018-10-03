import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('get_most_recently_used_history')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Returns the current user's most recently used history (not deleted).

Output:

    
    """
    return ctx.gi.histories.get_most_recently_used_history()
