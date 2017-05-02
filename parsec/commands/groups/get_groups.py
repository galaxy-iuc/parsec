import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_groups')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get all (not deleted) groups.
    """
    return ctx.gi.groups.get_groups()
