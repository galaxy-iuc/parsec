import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_history')

@click.option(
    "--name",
    help="Optional name for new history",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, name=""):
    """Create a new history, optionally setting the ``name``.
    """
    return ctx.gi.histories.create_history(name=name)
