import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('create_local_user')
@click.argument("username", type=str, help="username of the user to be created")
@click.argument("user_email", type=str, help="email of the user to be created")
@click.argument("password", type=str, help="password of the user to be created")
@pass_context
@custom_exception
@json_output
def cli(ctx, username, user_email, password):
    """Create a new Galaxy local user.

Output:

    a dictionary containing information about the created user
    """
    return ctx.gi.users.create_local_user(username, user_email, password)
