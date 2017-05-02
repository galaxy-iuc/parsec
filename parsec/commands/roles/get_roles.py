import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_roles')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Displays a collection (list) of roles.
    """
    return ctx.gi.roles.get_roles()
