import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('get_genomes')


@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Returns a list of installed genomes

Output:

    
    """
    return ctx.gi.genomes.get_genomes()
