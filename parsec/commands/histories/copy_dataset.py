import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('copy_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--source",
    help="Source of the dataset to be copied: 'hda' (the default), 'library' or 'library_folder'",
    default="hda",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, dataset_id, source="hda"):
    """Copy a dataset to a history.

Output:

    Information about the copied dataset
    """
    return ctx.gi.histories.copy_dataset(history_id, dataset_id, source=source)
