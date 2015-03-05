import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('visual_get_visualizations')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of visualizations
    """
    return ctx.gi.visual.get_visualizations()
