import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_visualizations')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of all visualizations.

Output:

    A list of dicts with details on individual visualizations.
          For example::

            [{u'dbkey': u'eschColi_K12',
              u'id': u'df1c7c96fc427c2d',
              u'title': u'AVTest1',
              u'type': u'trackster',
              u'url': u'/api/visualizations/df1c7c96fc427c2d'},
             {u'dbkey': u'mm9',
              u'id': u'a669f50f8bf55b02',
              u'title': u'Bam to Bigwig',
              u'type': u'trackster',
              u'url': u'/api/visualizations/a669f50f8bf55b02'}]
    """
    return ctx.gi.visual.get_visualizations()
