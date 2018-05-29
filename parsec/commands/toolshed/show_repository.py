import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output

@click.command('show_repository')
@click.argument("toolShed_id", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, toolShed_id):
    """Get details of a given Tool Shed repository as it is installed on this Galaxy instance.
    """
    return ctx.gi.toolshed.show_repository(toolShed_id)
