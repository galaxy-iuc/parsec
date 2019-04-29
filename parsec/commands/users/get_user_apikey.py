import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('get_user_apikey')
@click.argument("user_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, user_id):
    """Get the current API key for a given user. This functionality is available since Galaxy ``release_17.01``.

Output:

    the API key for the user
    """
    return ctx.gi.users.get_user_apikey(user_id)
