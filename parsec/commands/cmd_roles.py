import click
from parsec.commands.roles.create_role import cli as create_role
from parsec.commands.roles.get_roles import cli as get_roles
from parsec.commands.roles.show_role import cli as show_role


@click.group()
def cli():
    pass


cli.add_command(create_role)
cli.add_command(get_roles)
cli.add_command(show_role)
