import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_create_user')
@options.galaxy_instance()
@click.argument("user_email", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, user_email):
    """Deprecated method.
    """
    return ctx.gi.users.create_user(user_email)
