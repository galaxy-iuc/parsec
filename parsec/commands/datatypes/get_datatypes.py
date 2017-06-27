import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output, _arg_split

@click.command('get_datatypes')

@click.option(
    "--extension_only",
    help=""
)
@click.option(
    "--upload_only",
    help=""
)

@pass_context
@custom_exception
@list_output
def cli(ctx, extension_only=False, upload_only=False):
    """Get the list of all installed datatypes.

Output:

     A list of datatype names.
          For example::

            [u'snpmatrix',
             u'snptest',
             u'tabular',
             u'taxonomy',
             u'twobit',
             u'txt',
             u'vcf',
             u'wig',
             u'xgmml',
             u'xml']
        
    """
    return ctx.gi.datatypes.get_datatypes(extension_only=extension_only, upload_only=upload_only)
