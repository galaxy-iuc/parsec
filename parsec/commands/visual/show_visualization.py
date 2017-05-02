import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_visualization')
@click.argument("visual_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, visual_id):
    """Get details of a given visualization.
    """
    return ctx.gi.visual.show_visualization(visual_id)
