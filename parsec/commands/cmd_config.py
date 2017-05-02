import click
from parsec.commands.config.init import cli as func0
from parsec.commands.config.cmd_config_init import cli as func1
from parsec.commands.config.get_config import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
