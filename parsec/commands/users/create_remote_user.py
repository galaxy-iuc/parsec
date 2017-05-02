import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_remote_user')
@click.argument("user_email", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user_email):
    """Create a new Galaxy remote user.
    """
    return ctx.gi.users.create_remote_user(user_email)
