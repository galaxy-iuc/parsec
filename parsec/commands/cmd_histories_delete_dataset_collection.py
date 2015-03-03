import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_delete_dataset_collection')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("dataset_collection_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, dataset_collection_id):
    """Mark corresponding dataset collection as deleted.
    """
    return ctx.gi.histories.delete_dataset_collection(history_id, dataset_collection_id)
