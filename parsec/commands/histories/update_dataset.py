import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('update_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--annotation",
    help="Replace history dataset annotation with given string",
    type=str
)
@click.option(
    "--deleted",
    help="Mark or unmark history dataset as deleted",
    is_flag=True
)
@click.option(
    "--genome_build",
    help="Replace history dataset genome build (dbkey)",
    type=str
)
@click.option(
    "--name",
    help="Replace history dataset name with the given string",
    type=str
)
@click.option(
    "--visible",
    help="Mark or unmark history dataset as visible",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, dataset_id, annotation=None, deleted=None, genome_build=None, name=None, visible=None):
    """Update history dataset metadata. Some of the attributes that can be modified are documented below.
    """
    kwargs = {}
    if annotation and len(annotation) > 0:
        kwargs['annotation'] = annotation
    if deleted is not None:
        kwargs['deleted'] = deleted
    if genome_build and len(genome_build) > 0:
        kwargs['genome_build'] = genome_build
    if name and len(name) > 0:
        kwargs['name'] = name
    if visible is not None:
        kwargs['visible'] = visible

    return ctx.gi.histories.update_dataset(history_id, dataset_id, **kwargs)
