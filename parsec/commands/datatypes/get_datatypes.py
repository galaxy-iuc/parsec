import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_datatypes')
@click.option(
    "--extension_only",
    help="Return only the extension rather than the datatype name",
    is_flag=True
)
@click.option(
    "--upload_only",
    help="Whether to return only datatypes which can be uploaded",
    is_flag=True
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
