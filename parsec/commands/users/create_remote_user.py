import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_remote_user')
@click.argument("user_email", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user_email):
    """Create a new Galaxy remote user.

Output:

    a dictionary containing information about the created user
    """
    return ctx.gi.users.create_remote_user(user_email)
