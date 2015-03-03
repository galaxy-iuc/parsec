import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('roles_show_role')
@options.galaxy_instance()
@click.argument("role_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, role_id):
    """Display information on a single role
    """
    return ctx.gi.roles.show_role(role_id)
