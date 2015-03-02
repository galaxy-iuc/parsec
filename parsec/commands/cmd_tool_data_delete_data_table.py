import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tool_data_delete_data_table')
@options.galaxy_instance()
@click.argument("data_table_id", type=str)
@click.argument("values", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, data_table_id, values):
    """Delete an item from a data table.
    """
    return ctx.gi.tool_data.delete_data_table(data_table_id, values)