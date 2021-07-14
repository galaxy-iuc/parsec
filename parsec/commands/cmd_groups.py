import click
from parsec.commands.groups.add_group_role import cli as add_group_role
from parsec.commands.groups.add_group_user import cli as add_group_user
from parsec.commands.groups.create_group import cli as create_group
from parsec.commands.groups.delete_group_role import cli as delete_group_role
from parsec.commands.groups.delete_group_user import cli as delete_group_user
from parsec.commands.groups.get_group_roles import cli as get_group_roles
from parsec.commands.groups.get_group_users import cli as get_group_users
from parsec.commands.groups.get_groups import cli as get_groups
from parsec.commands.groups.show_group import cli as show_group
from parsec.commands.groups.update_group import cli as update_group


@click.group()
def cli():
    pass


cli.add_command(add_group_role)
cli.add_command(add_group_user)
cli.add_command(create_group)
cli.add_command(delete_group_role)
cli.add_command(delete_group_user)
cli.add_command(get_group_roles)
cli.add_command(get_group_users)
cli.add_command(get_groups)
cli.add_command(show_group)
cli.add_command(update_group)
