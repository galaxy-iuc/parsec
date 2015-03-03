import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tool_data_get_data_tables')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Displays a collection (list) of data tables.
    """
    return ctx.gi.tool_data.get_data_tables()
