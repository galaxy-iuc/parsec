import click

from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('users_create_user')
@click.argument("user_email")
@pass_context
@custom_exception
@dict_output
def cli(ctx, user_email):
    """Deprecated method.
    """
    return ctx.gi.users.create_user(user_email)
