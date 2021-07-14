import click
from parsec.commands.toolshed.get_repositories import cli as get_repositories
from parsec.commands.toolshed.install_repository_revision import cli as install_repository_revision
from parsec.commands.toolshed.show_repository import cli as show_repository
from parsec.commands.toolshed.uninstall_repository_revision import cli as uninstall_repository_revision


@click.group()
def cli():
    pass


cli.add_command(get_repositories)
cli.add_command(install_repository_revision)
cli.add_command(show_repository)
cli.add_command(uninstall_repository_revision)
