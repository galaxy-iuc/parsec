import click
from parsec.commands.toolshed_repositories.create_repository import cli as func0
from parsec.commands.toolshed_repositories.get_ordered_installable_revisions import cli as func1
from parsec.commands.toolshed_repositories.get_repositories import cli as func2
from parsec.commands.toolshed_repositories.get_repository_revision_install_info import cli as func3
from parsec.commands.toolshed_repositories.repository_revisions import cli as func4
from parsec.commands.toolshed_repositories.search_repositories import cli as func5
from parsec.commands.toolshed_repositories.show_repository import cli as func6
from parsec.commands.toolshed_repositories.show_repository_revision import cli as func7
from parsec.commands.toolshed_repositories.update_repository import cli as func8

@click.group()
def cli():
    pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
cli.add_command(func8)
