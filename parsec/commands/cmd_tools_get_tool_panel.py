import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_get_tool_panel')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Get a list of available tool elements in Galaxy's configured toolbox.
    """
    return ctx.gi.tools.get_tool_panel()
