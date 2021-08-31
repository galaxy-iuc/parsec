import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_visualization')
@click.argument("visual_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, visual_id):
    """Get details of a given visualization.

Output:

    A description of the given visualization.
          For example::

            {'annotation': None,
             'dbkey': 'mm9',
             'id': '18df9134ea75e49c',
             'latest_revision': {  ... },
             'model_class': 'Visualization',
             'revisions': ['aa90649bb3ec7dcb', '20622bc6249c0c71'],
             'slug': 'visualization-for-grant-1',
             'title': 'Visualization For Grant',
             'type': 'trackster',
             'url': '/u/azaron/v/visualization-for-grant-1',
             'user_id': '21e4aed91386ca8b'}
    """
    return ctx.gi.visual.show_visualization(visual_id)
