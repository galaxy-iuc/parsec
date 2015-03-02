import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets_show_stderr')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Display stderr output of a dataset.
    """
    return ctx.gi.datasets.show_stderr()