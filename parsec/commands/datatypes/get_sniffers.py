import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_sniffers')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of all installed sniffers.

Output:

    A list of sniffer names.
          For example::

            [u'galaxy.datatypes.tabular:Vcf',
             u'galaxy.datatypes.binary:TwoBit',
             u'galaxy.datatypes.binary:Bam',
             u'galaxy.datatypes.binary:Sff',
             u'galaxy.datatypes.xml:Phyloxml',
             u'galaxy.datatypes.xml:GenericXml',
             u'galaxy.datatypes.sequence:Maf',
             u'galaxy.datatypes.sequence:Lav',
             u'galaxy.datatypes.sequence:csFasta']
    """
    return ctx.gi.datatypes.get_sniffers()
