import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('reload_data_table')
@click.argument("data_table_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, data_table_id):
    """Reload a data table.
    """
    return ctx.gi.tool_data.reload_data_table(data_table_id)
