import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_data_tables')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of all data tables.
    """
    return ctx.gi.tool_data.get_data_tables()
