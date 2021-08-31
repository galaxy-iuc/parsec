import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


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
@click.option(
    "--name",
    help="Dataset name to filter on.",
    type=str
)
@click.option(
    "--extension",
    help="Dataset extension (or list of extensions) to filter on."
)
@click.option(
    "--state",
    help="Dataset state (or list of states) to filter on."
)
@click.option(
    "--visible",
    help="Optionally filter datasets by their ``visible`` attribute.",
    is_flag=True
)
@click.option(
    "--deleted",
    help="Optionally filter datasets by their ``deleted`` attribute.",
    is_flag=True
)
@click.option(
    "--purged",
    help="Optionally filter datasets by their ``purged`` attribute.",
    is_flag=True
)
@click.option(
    "--tool_id",
    help="Tool ID to filter on.",
    type=str
)
@click.option(
    "--tag",
    help="Dataset tag to filter on.",
    type=str
)
@click.option(
    "--history_id",
    help="Encoded history ID to filter on.",
    type=str
)
@click.option(
    "--create_time_min",
    help="Show only datasets created after the provided time and date, which should be formatted as ``YYYY-MM-DDTHH-MM-SS``.",
    type=str
)
@click.option(
    "--create_time_max",
    help="Show only datasets created before the provided time and date, which should be formatted as ``YYYY-MM-DDTHH-MM-SS``.",
    type=str
)
@click.option(
    "--update_time_min",
    help="Show only datasets last updated after the provided time and date, which should be formatted as ``YYYY-MM-DDTHH-MM-SS``.",
    type=str
)
@click.option(
    "--update_time_max",
    help="Show only datasets last updated before the provided time and date, which should be formatted as ``YYYY-MM-DDTHH-MM-SS``.",
    type=str
)
@click.option(
    "--order",
    help="One or more of the following attributes for ordering datasets: ``create_time`` (default), ``extension``, ``hid``, ``history_id``, ``name``, ``update_time``. Optionally, ``-asc`` or ``-dsc`` (default) can be appended for ascending and descending order respectively. Multiple attributes can be stacked as a comma-separated list of values, e.g. ``create_time-asc,hid-dsc``.",
    default="create_time-dsc",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, limit=500, offset=0, name="", extension="", state="", visible="", deleted="", purged="", tool_id="", tag="", history_id="", create_time_min="", create_time_max="", update_time_min="", update_time_max="", order="create_time-dsc"):
    """Get the latest datasets, or select another subset by specifying optional arguments for filtering (e.g. a history ID).

Output:

    
    """
    return ctx.gi.datasets.get_datasets(limit=limit, offset=offset, name=name, extension=extension, state=state, visible=visible, deleted=deleted, purged=purged, tool_id=tool_id, tag=tag, history_id=history_id, create_time_min=create_time_min, create_time_max=create_time_max, update_time_min=update_time_min, update_time_max=update_time_max, order=order)
