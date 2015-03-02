import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('visual_show_visualization')
@options.galaxy_instance()
@click.argument("visual_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, visual_id):
    """Display information on a visualization
    """
    return ctx.gi.visual.show_visualization(visual_id)
