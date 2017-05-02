import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('tool_data_get_data_tables')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Displays a collection (list) of data tables.
    """
    return ctx.gi.tool_data.get_data_tables()
