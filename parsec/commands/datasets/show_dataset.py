import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_dataset')
@click.argument("dataset_id", type=str)
@click.option(
    "--deleted",
    help="Whether to return results for a deleted dataset",
    is_flag=True
)
@click.option(
    "--hda_ldda",
    help="Whether to show a history dataset ('hda' - the default) or library dataset ('ldda').",
    default="hda",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, dataset_id, deleted=False, hda_ldda="hda"):
    """Get details about a given dataset. This can be a history or a library dataset.

Output:

    Information about the HDA or LDDA
    """
    return ctx.gi.datasets.show_dataset(dataset_id, deleted=deleted, hda_ldda=hda_ldda)
