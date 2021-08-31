import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('update_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--annotation",
    help="Replace history dataset annotation with given string",
    type=str
)
@click.option(
    "--datatype",
    help="Replace the datatype of the history dataset with the given string. The string must be a valid Galaxy datatype, both the current and the target datatypes must allow datatype changes, and the dataset must not be in use as input or output of a running job (including uploads), otherwise an error will be raised.",
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
@custom_exception
@json_output
def cli(ctx, history_id, dataset_id, annotation=None, datatype=None, deleted=None, genome_build=None, name=None, visible=None):
    """Update history dataset metadata. Some of the attributes that can be modified are documented below.

Output:

    details of the updated dataset

        .. versionchanged:: 0.8.0
            Changed the return value from the status code (type int) to a dict.
    """
    kwargs = {}

    return ctx.gi.histories.update_dataset(history_id, dataset_id, **kwargs)
