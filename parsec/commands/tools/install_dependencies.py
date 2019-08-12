import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('install_dependencies')
@click.argument("tool_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, tool_id):
    """Install dependencies for a given tool via a resolver. This works only for Conda currently. This functionality is available since Galaxy release_16.10 and is available only to Galaxy admins.

Output:

    Tool requirement status
    """
    return ctx.gi.tools.install_dependencies(tool_id)
