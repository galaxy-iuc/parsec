import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('roles_get_roles')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Displays a collection (list) of roles.
    """
    return ctx.gi.roles.get_roles()