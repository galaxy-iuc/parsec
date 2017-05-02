import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('tools_get_tool_panel')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of available tool elements in Galaxy's configured toolbox.
    """
    return ctx.gi.tools.get_tool_panel()
