import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

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
    help="If True, mark history as purged (permanently deleted). Ignored on Galaxy release_15.01 and earlier",
    is_flag=True
)
@click.option(
    "--tags",
    help="Replace history tags with the given list",
    type=str,
    multiple=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, annotation=None, deleted=None, importable=None, name=None, published=None, purged=None, tags=None):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    kwargs = {}
    if annotation and len(annotation) > 0:
        kwargs['annotation'] = annotation
    if deleted is not None:
        kwargs['deleted'] = deleted
    if importable is not None:
        kwargs['importable'] = importable
    if name and len(name) > 0:
        kwargs['name'] = name
    if published is not None:
        kwargs['published'] = published
    if purged is not None:
        kwargs['purged'] = purged

    return ctx.gi.histories.update_history(history_id, tags=tags, **kwargs)
