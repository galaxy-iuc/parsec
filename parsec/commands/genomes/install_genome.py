import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('install_genome')

@click.option(
    "--func",
    help="Allowed values: 'download', Download and index; 'index', Index only",
    default="download",
    type=str
)
@click.option(
    "--source",
    help="Data source for this build. Can be: UCSC, Ensembl, NCBI, URL",
    type=str
)
@click.option(
    "--dbkey",
    help="DB key of the build to download, ignored unless 'UCSC' is specified as the source",
    type=str
)
@click.option(
    "--ncbi_name",
    help="NCBI's genome identifier, ignored unless NCBI is specified as the source",
    type=str
)
@click.option(
    "--ensembl_dbkey",
    help="Ensembl's genome identifier, ignored unless Ensembl is specified as the source",
    type=str
)
@click.option(
    "--url_dbkey",
    help="DB key to use for this build, ignored unless URL is specified as the source",
    type=str
)
@click.option(
    "--indexers",
    help="POST array of indexers to run after downloading (indexers[] = first, indexers[] = second, ...)",
    type=str,
    multiple=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, func="download", source="", dbkey="", ncbi_name="", ensembl_dbkey="", url_dbkey="", indexers=""):
    """Download and/or index a genome.
    """
    return ctx.gi.genomes.install_genome(func=func, source=source, dbkey=dbkey, ncbi_name=ncbi_name, ensembl_dbkey=ensembl_dbkey, url_dbkey=url_dbkey, indexers=indexers)
