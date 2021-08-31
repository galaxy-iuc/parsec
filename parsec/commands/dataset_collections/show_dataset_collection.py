import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_dataset_collection')
@click.argument("dataset_collection_id", type=str)
@click.option(
    "--instance_type",
    help="instance type of the collection - 'history' or 'library'",
    default="history",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_collection_id, instance_type="history"):
    """Get details of a given dataset collection of the current user

Output:

    element view of the dataset collection
    """
    return ctx.gi.dataset_collections.show_dataset_collection(dataset_collection_id, instance_type=instance_type)
