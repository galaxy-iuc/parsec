import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_stderr')
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, dataset_id):
    """Get the stderr output of a dataset.
    """
    return ctx.gi.datasets.show_stderr(dataset_id)
