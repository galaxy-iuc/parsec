import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('tool_data.show_data_table')
@options.galaxy_instance()

@click.argument("data_table_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, data_table_id):
    """Display information on a single data_table
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tool_data.show_data_table(data_table_id)

