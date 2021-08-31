import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_histories')
@click.option(
    "--history_id",
    help="Encoded history ID to filter on",
    type=str
)
@click.option(
    "--name",
    help="History name to filter on.",
    type=str
)
@click.option(
    "--deleted",
    help="whether to filter for the deleted histories (``True``) or for the non-deleted ones (``False``)",
    is_flag=True
)
@click.option(
    "--published",
    help="whether to filter for the published histories (``True``) or for the non-published ones (``False``). If not set, no filtering is applied. Note the filtering is only applied to the user's own histories; to access all histories published by any user, use the ``get_published_histories`` method.",
    is_flag=True
)
@click.option(
    "--slug",
    help="History slug to filter on",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id="", name="", deleted=False, published="", slug=""):
    """Get all histories, or select a subset by specifying optional arguments for filtering (e.g. a history name).

Output:

    List of history dicts.
    """
    return ctx.gi.histories.get_histories(history_id=history_id, name=name, deleted=deleted, published=published, slug=slug)
