import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_dataset_collection')
@click.argument("history_id", type=str)
@click.argument("collection_description")
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, collection_description):
    """Create a new dataset collection

Output:

    Information about the new HDCA
    """
    return ctx.gi.histories.create_dataset_collection(history_id, collection_description)
