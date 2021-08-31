import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('wait_for_dataset_collection')
@click.argument("dataset_collection_id", type=str)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the dataset states in the dataset collection to become terminal. If not all datasets are in a terminal state within this time, a ``DatasetCollectionTimeoutException`` will be raised.",
    default="12000",
    show_default=True,
    type=float
)
@click.option(
    "--interval",
    help="Time (in seconds) to wait between two consecutive checks.",
    default="3",
    show_default=True,
    type=float
)
@click.option(
    "--proportion_complete",
    help="Proportion of elements in this collection that have to be in a terminal state for this method to return. Must be a number between 0 and 1. For example: if the dataset collection contains 2 elements, and proportion_complete=0.5 is specified, then wait_for_dataset_collection will return as soon as 1 of the 2 datasets is in a terminal state. Default is 1, i.e. all elements must complete.",
    default="1.0",
    show_default=True,
    type=float
)
@click.option(
    "--check",
    help="Whether to check if all the terminal states of datasets in the dataset collection are 'ok'. This will raise an Exception if a dataset is in a terminal state other than 'ok'.",
    default="True",
    show_default=True,
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_collection_id, maxwait=12000, interval=3, proportion_complete=1.0, check=True):
    """Wait until all or a specified proportion of elements of a dataset collection are in a terminal state.

Output:

    Details of the given dataset collection.
    """
    return ctx.gi.dataset_collections.wait_for_dataset_collection(dataset_collection_id, maxwait=maxwait, interval=interval, proportion_complete=proportion_complete, check=check)
