import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_get_current_user')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Returns the user id associated with this Galaxy connection
    """
    return ctx.gi.users.get_current_user()
