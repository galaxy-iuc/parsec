import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('groups_get_groups')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Displays a collection (list) of groups.
    """
    return ctx.gi.groups.get_groups()
