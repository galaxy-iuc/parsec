import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_published_histories')
@click.option(
    "--name",
    help="Name of history to filter on",
    type=str
)
@click.option(
    "--deleted",
    help="whether to filter for the deleted histories (``True``) or for the non-deleted ones (``False``)",
    is_flag=True
)
@click.option(
    "--slug",
    help="History slug to filter on",
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, name="", deleted=False, slug=""):
    """Get all published histories (by any user) or filter the specific one(s) by ``name`` or other arguments.

Output:

    List of history dicts.
    """
    return ctx.gi.histories.get_published_histories(name=name, deleted=deleted, slug=slug)
