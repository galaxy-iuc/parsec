import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('wait_for_dataset')
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the dataset state to become terminal. If the dataset state is not terminal within this time, a ``DatasetTimeoutException`` will be thrown.",
    default="12000",
    show_default=True,
    type=float
)
@click.option(
    "--interval",
    help="Time (in seconds) to wait between 2 consecutive checks.",
    default="3",
    show_default=True,
    type=float
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, dataset_id, maxwait=12000, interval=3):
    """Wait until the library dataset state is terminal ('ok', 'empty', 'error', 'discarded' or 'failed_metadata').

Output:

    A dictionary containing information about the dataset in the
          library
    """
    return ctx.gi.libraries.wait_for_dataset(library_id, dataset_id, maxwait=maxwait, interval=interval)
