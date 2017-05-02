import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('datasets_show_stderr')
@click.argument("dataset_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, dataset_id):
    """Display stderr output of a dataset.
    """
    return ctx.gi.datasets.show_stderr(dataset_id)
