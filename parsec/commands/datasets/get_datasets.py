import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_datasets')
@click.option(
    "--limit",
    help="Maximum number of datasets to return.",
    default="500",
    show_default=True,
    type=int
)
@click.option(
    "--offset",
    help="Return datasets starting from this specified position. For example, if ``limit`` is set to 100 and ``offset`` to 200, datasets 200-299 will be returned.",
    type=int
)
@pass_context
@custom_exception
@list_output
def cli(ctx, limit=500, offset=0):
    """Provide a list of all datasets. Since this may be very large, ``limit`` and ``offset`` parameters should be used to specify the desired range.

Output:

    Return a list of dataset dicts.
    """
    return ctx.gi.datasets.get_datasets(limit=limit, offset=offset)
