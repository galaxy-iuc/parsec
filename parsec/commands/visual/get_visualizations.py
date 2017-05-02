import click
import json
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_visualizations')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of all visualizations.
    """
    return ctx.gi.visual.get_visualizations()
