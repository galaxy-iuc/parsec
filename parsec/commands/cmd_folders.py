import click
from parsec.commands.folders.show_folder import cli as func0
from parsec.commands.folders.delete_folder import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
