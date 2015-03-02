import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_show_tool')
@options.galaxy_instance()

@click.option(
    "--tool_id",
    help="id of the requested tool",
    type=str
)
@click.option(
    "--io_details",
    help="if True, get also input and output details",
    type=bool
)
@click.option(
    "--link_details",
    help="if True, get also link details",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, tool_id=False, io_details=False, link_details=False):
    """Get details of a given tool.
    """
    return ctx.gi.tools.show_tool(tool_id=tool_id, io_details=io_details, link_details=link_details)
