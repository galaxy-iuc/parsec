import click
from parsec.commands.tool_data.delete_data_table import cli as delete_data_table
from parsec.commands.tool_data.get_data_tables import cli as get_data_tables
from parsec.commands.tool_data.reload_data_table import cli as reload_data_table
from parsec.commands.tool_data.show_data_table import cli as show_data_table


@click.group()
def cli():
    pass


cli.add_command(delete_data_table)
cli.add_command(get_data_tables)
cli.add_command(reload_data_table)
cli.add_command(show_data_table)
