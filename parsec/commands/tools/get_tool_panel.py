import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_tool_panel')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get a list of available tool elements in Galaxy's configured toolbox.

Output:

    List containing tools (if not in sections) or tool sections
                 with nested tool descriptions.

        .. seealso:: bioblend.galaxy.toolshed.get_repositories()
    """
    return ctx.gi.tools.get_tool_panel()
