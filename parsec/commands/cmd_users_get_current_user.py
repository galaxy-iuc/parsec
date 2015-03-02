import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_get_current_user')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """Returns the user id associated with this Galaxy connection
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.users.get_current_user()

