import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('delete_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--purge",
    help="if ``True``, also purge (permanently delete) the dataset",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, dataset_id, purge=False):
    """Mark corresponding dataset as deleted.
    """
    return ctx.gi.histories.delete_dataset(history_id, dataset_id, purge=purge)
