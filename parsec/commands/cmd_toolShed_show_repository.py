import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('toolShed_show_repository')
@click.argument("toolShed_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, toolShed_id):
    """Display information of a repository from the Tool Shed
    """
    return ctx.gi.toolShed.show_repository(toolShed_id)
