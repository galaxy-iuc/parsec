import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_tool')
@click.argument("tool_id", type=str)

@click.option(
    "--io_details",
    help="if True, get also input and output details",
    is_flag=True
)
@click.option(
    "--link_details",
    help="if True, get also link details",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, tool_id, io_details=False, link_details=False):
    """Get details of a given tool.
    """
    return ctx.gi.tools.show_tool(tool_id, io_details=io_details, link_details=link_details)
