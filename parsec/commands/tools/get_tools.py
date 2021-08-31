import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_tools')
@click.option(
    "--tool_id",
    help="id of the requested tool",
    type=str
)
@click.option(
    "--name",
    help="Tool name to filter on.",
    type=str
)
@click.option(
    "--trackster",
    help="whether to return only tools that are compatible with Trackster",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, tool_id="", name="", trackster=""):
    """Get all tools, or select a subset by specifying optional arguments for filtering (e.g. a tool name).

Output:

    List of tool descriptions.

        .. seealso:: bioblend.galaxy.toolshed.get_repositories()
    """
    return ctx.gi.tools.get_tools(tool_id=tool_id, name=name, trackster=trackster)
