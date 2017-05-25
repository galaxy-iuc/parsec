import click
from parsec.commands.folders.create_folder import cli as func0
from parsec.commands.folders.delete_folder import cli as func1
from parsec.commands.folders.get_permissions import cli as func2
from parsec.commands.folders.set_permissions import cli as func3
from parsec.commands.folders.show_folder import cli as func4
from parsec.commands.folders.update_folder import cli as func5

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
