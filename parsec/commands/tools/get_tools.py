import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_tools')
@click.option(
    "--tool_id",
    help="id of the requested tool",
    type=str
)
@click.option(
    "--name",
    help="name of the requested tool(s)",
    type=str
)
@click.option(
    "--trackster",
    help="whether to return only tools that are compatible with Trackster",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, tool_id="", name="", trackster=""):
    """Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.

Output:

    List of tool descriptions.

        .. seealso:: bioblend.galaxy.toolshed.get_repositories()
    """
    return ctx.gi.tools.get_tools(tool_id=tool_id, name=name, trackster=trackster)
