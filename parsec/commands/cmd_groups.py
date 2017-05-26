import click
from parsec.commands.groups.add_group_role import cli as func0
from parsec.commands.groups.add_group_user import cli as func1
from parsec.commands.groups.create_group import cli as func2
from parsec.commands.groups.delete_group_role import cli as func3
from parsec.commands.groups.delete_group_user import cli as func4
from parsec.commands.groups.get_group_roles import cli as func5
from parsec.commands.groups.get_group_users import cli as func6
from parsec.commands.groups.get_groups import cli as func7
from parsec.commands.groups.show_group import cli as func8
from parsec.commands.groups.update_group import cli as func9

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
cli.add_command(func9)
