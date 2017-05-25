import click
from parsec.commands.tool_data.delete_data_table import cli as func0
from parsec.commands.tool_data.get_data_tables import cli as func1
from parsec.commands.tool_data.reload_data_table import cli as func2
from parsec.commands.tool_data.show_data_table import cli as func3

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
