
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_history')
@options.galaxy_instance()

@click.argument("name", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, name):
    """Create a new history, optionally setting the ``name``.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.create_history(name)
