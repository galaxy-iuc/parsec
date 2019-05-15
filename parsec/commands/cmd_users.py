import click
from parsec.commands.users.create_local_user import cli as create_local_user
from parsec.commands.users.create_remote_user import cli as create_remote_user
from parsec.commands.users.create_user_apikey import cli as create_user_apikey
from parsec.commands.users.delete_user import cli as delete_user
from parsec.commands.users.get_current_user import cli as get_current_user
from parsec.commands.users.get_user_apikey import cli as get_user_apikey
from parsec.commands.users.get_users import cli as get_users
from parsec.commands.users.show_user import cli as show_user


@click.group()
def cli():
    pass


cli.add_command(create_local_user)
cli.add_command(create_remote_user)
cli.add_command(create_user_apikey)
cli.add_command(delete_user)
cli.add_command(get_current_user)
cli.add_command(get_user_apikey)
cli.add_command(get_users)
cli.add_command(show_user)
