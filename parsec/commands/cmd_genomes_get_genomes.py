import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('genomes_get_genomes')
@options.galaxy_instance()



@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance):
    """Returns a list of installed genomes
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.genomes.get_genomes()

