import click
from parsec.commands.toolshed.get_repositories import cli as func0
from parsec.commands.toolshed.install_repository_revision import cli as func1
from parsec.commands.toolshed.show_repository import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
