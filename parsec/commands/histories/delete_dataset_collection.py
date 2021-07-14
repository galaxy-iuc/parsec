import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, none_output


@click.command('delete_dataset_collection')
@click.argument("history_id", type=str)
@click.argument("dataset_collection_id", type=str)
@pass_context
@custom_exception
@none_output
def cli(ctx, history_id, dataset_collection_id):
    """Mark corresponding dataset collection as deleted.

Output:

    None
    """
    return ctx.gi.histories.delete_dataset_collection(history_id, dataset_collection_id)
