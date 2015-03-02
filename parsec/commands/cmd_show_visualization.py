
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_visualization')
@options.galaxy_instance()

@click.argument("visual_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, visual_id):
    """Display information on a visualization
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.visual.show_visualization(visual_id)
