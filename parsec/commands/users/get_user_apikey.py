import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_user_apikey')
@click.argument("user_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user_id):
    """Get the current API key for a given user. This functionality is available since Galaxy ``release_17.01``.
    """
    return ctx.gi.users.get_user_apikey(user_id)
