import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_sniffers')
@pass_context
@custom_exception
@json_output
def cli(ctx):
    """Get the list of all installed sniffers.

Output:

    A list of sniffer names.
          For example::

            ['galaxy.datatypes.tabular:Vcf',
             'galaxy.datatypes.binary:TwoBit',
             'galaxy.datatypes.binary:Bam',
             'galaxy.datatypes.binary:Sff',
             'galaxy.datatypes.xml:Phyloxml',
             'galaxy.datatypes.xml:GenericXml',
             'galaxy.datatypes.sequence:Maf',
             'galaxy.datatypes.sequence:Lav',
             'galaxy.datatypes.sequence:csFasta']
    """
    return ctx.gi.datatypes.get_sniffers()
