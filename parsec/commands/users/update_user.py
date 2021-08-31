import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('update_user')
@click.argument("user_id", type=str)
@click.option(
    "--email",
    help="Replace user email with the given string",
    type=str
)
@click.option(
    "--username",
    help="Replace user name with the given string",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, user_id, email=None, username=None):
    """Update user information. Some of the attributes that can be modified are documented below.

Output:

    details of the updated user
    """
    kwargs = {}

    return ctx.gi.users.update_user(user_id, **kwargs)
