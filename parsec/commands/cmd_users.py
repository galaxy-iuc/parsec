import click
from parsec.commands.users.create_local_user import cli as func0
from parsec.commands.users.create_remote_user import cli as func1
from parsec.commands.users.create_user import cli as func2
from parsec.commands.users.create_user_apikey import cli as func3
from parsec.commands.users.delete_user import cli as func4
from parsec.commands.users.get_current_user import cli as func5
from parsec.commands.users.get_user_apikey import cli as func6
from parsec.commands.users.get_users import cli as func7
from parsec.commands.users.show_user import cli as func8

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
