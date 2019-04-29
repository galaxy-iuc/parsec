import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('get_current_user')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Display information about the user associated with this Galaxy connection.

Output:

    a dictionary containing information about the current user
    """
    return ctx.gi.users.get_current_user()
