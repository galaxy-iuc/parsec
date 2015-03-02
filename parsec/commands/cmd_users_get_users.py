import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('users_get_users')
@options.galaxy_instance()

@click.option(
    "--deleted",
    help="None"
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, deleted=False):
    """Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.
    """
    return ctx.gi.users.get_users(deleted=deleted)