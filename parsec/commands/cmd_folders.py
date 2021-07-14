import click
from parsec.commands.folders.create_folder import cli as create_folder
from parsec.commands.folders.delete_folder import cli as delete_folder
from parsec.commands.folders.get_permissions import cli as get_permissions
from parsec.commands.folders.set_permissions import cli as set_permissions
from parsec.commands.folders.show_folder import cli as show_folder
from parsec.commands.folders.update_folder import cli as update_folder


@click.group()
def cli():
    pass


cli.add_command(create_folder)
cli.add_command(delete_folder)
cli.add_command(get_permissions)
cli.add_command(set_permissions)
cli.add_command(show_folder)
cli.add_command(update_folder)
