import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('toolshed_show_repository')
@click.argument("toolshed_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, toolshed_id):
    """Display information of a repository from the Tool Shed
    """
    return ctx.ti.repositories.show_repository(toolshed_id)
