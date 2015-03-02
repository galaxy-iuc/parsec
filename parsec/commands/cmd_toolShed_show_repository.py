import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('toolShed_show_repository')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Display information of a repository from the Tool Shed
    """
    return ctx.gi.toolShed.show_repository()
