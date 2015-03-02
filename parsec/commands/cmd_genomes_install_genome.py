import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('genomes_install_genome')
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
    return ctx.gi.genomes.install_genome(func, dbkey, ncbi_name, ensembl_dbkey, url_dbkey, indexers, source=source)
