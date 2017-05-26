import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_current_history')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """.. deprecated:: 0.5.2 Use :meth:`get_most_recently_used_history` instead.
    """
    return ctx.gi.histories.get_current_history()
