
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_genome')
@options.galaxy_instance()

@click.argument("id", type=str)
@click.argument("num", type=str)
@click.argument("chrom", type=str)
@click.argument("low", type=str)
@click.argument("high", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, id, num, chrom, low, high):
    """Returns information about build <id>
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.genomes.show_genome(id, num, chrom, low, high)
