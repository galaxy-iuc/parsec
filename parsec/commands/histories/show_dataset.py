import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_dataset')
@click.argument("history_id", type=str, help="Encoded history ID")
@click.argument("dataset_id", type=str, help="Encoded dataset ID")
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, dataset_id):
    """Get details about a given history dataset.

Output:

    Information about the dataset
    """
    return ctx.gi.histories.show_dataset(history_id, dataset_id)
