import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('update_dataset_collection')
@click.argument("history_id", type=str)
@click.argument("dataset_collection_id", type=str)

@click.option(
    "--deleted",
    help="Mark or unmark history dataset collection as deleted",
    is_flag=True
)
@click.option(
    "--name",
    help="Replace history dataset collection name with the given string",
    type=str
)
@click.option(
    "--visible",
    help="Mark or unmark history dataset collection as visible",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, dataset_collection_id, deleted=None, name=None, visible=None):
    """Update history dataset collection metadata. Some of the attributes that can be modified are documented below.
    """
    kwargs = {}
    if deleted is not None:
        kwargs['deleted'] = deleted
    if name and len(name) > 0:
        kwargs['name'] = name
    if visible is not None:
        kwargs['visible'] = visible

    return ctx.gi.histories.update_dataset_collection(history_id, dataset_collection_id, **kwargs)
