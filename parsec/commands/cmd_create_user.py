
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_user')
@options.galaxy_instance()

@click.argument("user_email", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, user_email):
    """Deprecated method.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.users.create_user(user_email)
