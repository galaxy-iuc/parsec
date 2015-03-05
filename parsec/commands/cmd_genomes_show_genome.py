import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('genomes_show_genome')
@click.argument("id", type=str)
@click.option(
    "--num",
    help="num",
    type=str
)
@click.option(
    "--chrom",
    help="chrom",
    type=str
)
@click.option(
    "--low",
    help="low",
    type=str
)
@click.option(
    "--high",
    help="high",
    type=str
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, id, num="", chrom="", low="", high=""):
    """Returns information about build <id>
    """
    return ctx.gi.genomes.show_genome(
        id,
        num=num,
        chrom=chrom,
        low=low,
        high=high)
