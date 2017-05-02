import click
from parsec.commands.quotas.get_quotas import cli as func0
from parsec.commands.quotas.show_quota import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
