import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_current_user')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Display information about the user associated with this Galaxy connection.
    """
    return ctx.gi.users.get_current_user()
