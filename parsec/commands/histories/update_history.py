import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('update_history')
@click.argument("history_id", type=str)
@click.option(
    "--annotation",
    help="Replace history annotation with given string",
    type=str
)
@click.option(
    "--deleted",
    help="Mark or unmark history as deleted",
    is_flag=True
)
@click.option(
    "--importable",
    help="Mark or unmark history as importable",
    is_flag=True
)
@click.option(
    "--name",
    help="Replace history name with the given string",
    type=str
)
@click.option(
    "--published",
    help="Mark or unmark history as published",
    is_flag=True
)
@click.option(
    "--purged",
    help="If ``True``, mark history as purged (permanently deleted).",
    is_flag=True
)
@click.option(
    "--tags",
    help="Replace history tags with the given list",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, annotation=None, deleted=None, importable=None, name=None, published=None, purged=None, tags=None):
    """Update history metadata information. Some of the attributes that can be modified are documented below.

Output:

    details of the updated history

        .. versionchanged:: 0.8.0
            Changed the return value from the status code (type int) to a dict.
    """
    kwargs = {}

    return ctx.gi.histories.update_history(history_id, tags=tags, **kwargs)
