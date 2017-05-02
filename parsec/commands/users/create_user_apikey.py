import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_user_apikey')
@click.argument("user_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user_id):
    """Create a new API key for a given user.
    """
    return ctx.gi.users.create_user_apikey(user_id)
