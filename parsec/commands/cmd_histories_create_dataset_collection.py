import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_create_dataset_collection')
@click.argument("history_id", type=str)
@click.argument("collection_description", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, collection_description):
    """Create a new dataset collection
    """
    return ctx.gi.histories.create_dataset_collection(
        history_id,
        collection_description)
