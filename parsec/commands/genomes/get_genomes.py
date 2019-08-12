import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_genomes')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Returns a list of installed genomes

Output:

    List of installed genomes
    """
    return ctx.gi.genomes.get_genomes()
