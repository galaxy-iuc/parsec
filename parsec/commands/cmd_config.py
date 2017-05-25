import click
from parsec.commands.config.get_config import cli as func0
from parsec.commands.config.get_version import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
