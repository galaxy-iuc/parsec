import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_update_dataset_collection')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("dataset_collection_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, dataset_collection_id):
    """Update history dataset collection metadata. Some of the attributes that can be modified are documented below.
    """
    return ctx.gi.histories.update_dataset_collection(history_id, dataset_collection_id)
