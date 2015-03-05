import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('datasets_show_stdout')
@click.argument("dataset_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, dataset_id):
    """Display stdout output of a dataset.
    """
    return ctx.gi.datasets.show_stdout(dataset_id)
