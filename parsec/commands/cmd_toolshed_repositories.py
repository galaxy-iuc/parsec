import click
from parsec.commands.toolshed_repositories.create_repository import cli as create_repository
from parsec.commands.toolshed_repositories.get_ordered_installable_revisions import cli as get_ordered_installable_revisions
from parsec.commands.toolshed_repositories.get_repositories import cli as get_repositories
from parsec.commands.toolshed_repositories.get_repository_revision_install_info import cli as get_repository_revision_install_info
from parsec.commands.toolshed_repositories.repository_revisions import cli as repository_revisions
from parsec.commands.toolshed_repositories.search_repositories import cli as search_repositories
from parsec.commands.toolshed_repositories.show_repository import cli as show_repository
from parsec.commands.toolshed_repositories.show_repository_revision import cli as show_repository_revision
from parsec.commands.toolshed_repositories.update_repository import cli as update_repository


@click.group()
def cli():
    pass


cli.add_command(create_repository)
cli.add_command(get_ordered_installable_revisions)
cli.add_command(get_repositories)
cli.add_command(get_repository_revision_install_info)
cli.add_command(repository_revisions)
cli.add_command(search_repositories)
cli.add_command(show_repository)
cli.add_command(show_repository_revision)
cli.add_command(update_repository)
