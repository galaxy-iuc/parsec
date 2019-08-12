import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('upload_dataset_from_library')
@click.argument("history_id", type=str)
@click.argument("lib_dataset_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, lib_dataset_id):
    """Upload a dataset into the history from a library. Requires the library dataset ID, which can be obtained from the library contents.

Output:

    Information about the newly created HDA
    """
    return ctx.gi.histories.upload_dataset_from_library(history_id, lib_dataset_id)
