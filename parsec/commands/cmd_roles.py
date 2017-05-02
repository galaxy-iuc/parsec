import click
from parsec.commands.roles.get_roles import cli as func0
from parsec.commands.roles.show_role import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
