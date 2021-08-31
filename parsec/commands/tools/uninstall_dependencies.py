import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('uninstall_dependencies')
@click.argument("tool_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, tool_id):
    """Uninstall dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available only to Galaxy admins.

Output:

    Tool requirement status
    """
    return ctx.gi.tools.uninstall_dependencies(tool_id)
