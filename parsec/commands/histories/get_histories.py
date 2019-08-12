import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_histories')
@click.option(
    "--history_id",
    help="Encoded history ID to filter on",
    type=str
)
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
@pass_context
@custom_exception
@list_output
def cli(ctx, history_id="", name="", deleted=False):
    """Get all histories or filter the specific one(s) via the provided ``name`` or ``history_id``. Provide only one argument, ``name`` or ``history_id``, but not both.

Output:

    Return a list of history element dicts. If more than one
                 history matches the given ``name``, return the list of all the
                 histories with the given name
    """
    return ctx.gi.histories.get_histories(history_id=history_id, name=name, deleted=deleted)
