import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('module')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """str(bytes_or_buffer[, encoding[, errors]]) -> str

Output:

    
    """
    return ctx.gi.datasets.module()
