import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_visualization')
@click.argument("visual_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, visual_id):
    """Get details of a given visualization.

Output:

    A description of the given visualization.
          For example::

            {u'annotation': None,
             u'dbkey': u'mm9',
             u'id': u'18df9134ea75e49c',
             u'latest_revision': {  ... },
             u'model_class': u'Visualization',
             u'revisions': [u'aa90649bb3ec7dcb', u'20622bc6249c0c71'],
             u'slug': u'visualization-for-grant-1',
             u'title': u'Visualization For Grant',
             u'type': u'trackster',
             u'url': u'/u/azaron/v/visualization-for-grant-1',
             u'user_id': u'21e4aed91386ca8b'}
    """
    return ctx.gi.visual.show_visualization(visual_id)
