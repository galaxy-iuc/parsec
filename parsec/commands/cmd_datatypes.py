import click
from parsec.commands.datatypes.get_datatypes import cli as func0
from parsec.commands.datatypes.get_sniffers import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
