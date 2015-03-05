import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_create_user')
@click.argument("user_email")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, user_email):
    """Deprecated method.
    """
    return ctx.gi.users.create_user(user_email)
