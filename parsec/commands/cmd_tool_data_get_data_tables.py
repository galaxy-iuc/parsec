import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('tool_data_get_data_tables')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """Displays a collection (list) of data tables.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tool_data.get_data_tables()

