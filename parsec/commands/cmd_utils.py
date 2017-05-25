import click
from parsec.commands.utils.wait_on_invocation import cli as func0

@click.group()
def cli():
	pass

cli.add_command(func0)
