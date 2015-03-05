import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_update_history')
@click.argument("history_id", type=str)
@click.option(
    "--name",
    help="Replace history name with the given string",
    type=str
)
@click.option(
    "--annotation",
    help="Replace history annotation with given string",
    type=str
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, name="", annotation=""):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    return ctx.gi.histories.update_history(
        history_id,
        name=name,
        annotation=annotation)
