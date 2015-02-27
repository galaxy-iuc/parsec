import click

from parsec.cli import pass_context
from parsec import options
import bioblend


@click.command('add_user')
@options.galaxy_instance()

@click.option(
    '--email',
    help="Email for the new user",
)

@click.option(
    '--password',
    help="Password for the new user",
)

@click.option(
    '--key',
    help="API key for the new user",
)
@pass_context
def cli(ctx, **kwds):
    """Add a user to a galaxy instance
    """
    print kwds
