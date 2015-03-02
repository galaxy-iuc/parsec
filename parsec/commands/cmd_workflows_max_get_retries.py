import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_max_get_retries')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """The maximum number of attempts for a GET request.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.max_get_retries()

