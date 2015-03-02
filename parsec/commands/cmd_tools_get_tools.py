import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_get_tools')
@options.galaxy_instance()

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
    help="if True, only tools that are compatible with Trackster are returned"
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, tool_id="", name="", trackster=""):
    """Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.
    """
    return ctx.gi.tools.get_tools(tool_id=tool_id, name=name, trackster=trackster)
