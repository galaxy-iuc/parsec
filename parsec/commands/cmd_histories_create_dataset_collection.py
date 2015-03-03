import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_create_dataset_collection')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("collection_description", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, collection_description):
    """Create a new dataset collection
    """
    return ctx.gi.histories.create_dataset_collection(history_id, collection_description)
