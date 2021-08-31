import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_history')
@click.argument("history_id", type=str)
@click.option(
    "--contents",
    help="When ``True``, instead of the history details, return a list with info for all datasets in the given history. Note that inside each dataset info dict, the id which should be used for further requests about this history dataset is given by the value of the `id` (not `dataset_id`) key.",
    is_flag=True
)
@click.option(
    "--deleted",
    help="When ``contents=True``, whether to filter for the deleted datasets (``True``) or for the non-deleted ones (``False``). If not set, no filtering is applied.",
    is_flag=True
)
@click.option(
    "--visible",
    help="When ``contents=True``, whether to filter for the visible datasets (``True``) or for the hidden ones (``False``). If not set, no filtering is applied.",
    is_flag=True
)
@click.option(
    "--details",
    help="When ``contents=True``, include dataset details. Set to 'all' for the most information.",
    type=str
)
@click.option(
    "--types",
    help="When ``contents=True``, filter for history content types. If set to ``['dataset']``, return only datasets. If set to ``['dataset_collection']``, return only dataset collections. If not set, no filtering is applied.",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, contents=False, deleted="", visible="", details="", types=""):
    """Get details of a given history. By default, just get the history meta information.

Output:

    details of the given history or list of dataset info

        .. note::
            As an alternative to using the ``contents=True`` parameter, consider
            using ``gi.datasets.get_datasets(history_id=history_id)`` which offers
            more extensive functionality for filtering and ordering the results.
    """
    return ctx.gi.histories.show_history(history_id, contents=contents, deleted=deleted, visible=visible, details=details, types=types)
