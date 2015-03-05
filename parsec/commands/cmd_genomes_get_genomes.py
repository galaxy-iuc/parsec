import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('genomes_get_genomes')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Returns a list of installed genomes
    """
    return ctx.gi.genomes.get_genomes()
