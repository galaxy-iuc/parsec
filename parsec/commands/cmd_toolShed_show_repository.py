import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('toolShed_show_repository')
@options.galaxy_instance()

@click.argument("toolShed_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, toolShed_id):
    """Display information of a repository from the Tool Shed
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.toolShed.show_repository(toolShed_id)

