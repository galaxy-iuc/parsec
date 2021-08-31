import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_visualizations')
@pass_context
@custom_exception
@json_output
def cli(ctx):
    """Get the list of all visualizations.

Output:

    A list of dicts with details on individual visualizations.
          For example::

            [{'dbkey': 'eschColi_K12',
              'id': 'df1c7c96fc427c2d',
              'title': 'AVTest1',
              'type': 'trackster',
              'url': '/api/visualizations/df1c7c96fc427c2d'},
             {'dbkey': 'mm9',
              'id': 'a669f50f8bf55b02',
              'title': 'Bam to Bigwig',
              'type': 'trackster',
              'url': '/api/visualizations/a669f50f8bf55b02'}]
    """
    return ctx.gi.visual.get_visualizations()
