import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_history')
@click.option(
    "--name",
    help="Optional name for new history",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, name=""):
    """Create a new history, optionally setting the ``name``.

Output:

    Dictionary containing information about newly created history
    """
    return ctx.gi.histories.create_history(name=name)
