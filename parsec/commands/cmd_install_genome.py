import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('genomes.install_genome')
@options.galaxy_instance()

@click.argument("func", type=str)
@click.argument("dbkey", type=str)
@click.argument("ncbi_name", type=str)
@click.argument("ensembl_dbkey", type=str)
@click.argument("url_dbkey", type=str)
@click.argument("indexers", type=list)

@click.option(
    "--source",
    help="Data source for this build. Can be: UCSC, Ensembl, NCBI, URL",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, func, dbkey, ncbi_name, ensembl_dbkey, url_dbkey, indexers, source=""):
    """Download and/or index a genome.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.genomes.install_genome(func, dbkey, ncbi_name, ensembl_dbkey, url_dbkey, indexers, source=source)

