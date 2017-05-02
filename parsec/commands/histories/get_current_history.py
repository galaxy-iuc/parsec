import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_current_history')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Deprecated method.
    """
    return ctx.gi.histories.get_current_history()
