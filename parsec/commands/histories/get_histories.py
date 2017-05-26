import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

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
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id="", name="", deleted=False):
    """Get all histories or filter the specific one(s) via the provided ``name`` or ``history_id``. Provide only one argument, ``name`` or ``history_id``, but not both.
    """
    return ctx.gi.histories.get_histories(history_id=history_id, name=name, deleted=deleted)
