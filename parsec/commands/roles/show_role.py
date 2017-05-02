import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_role')
@click.argument("role_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, role_id):
    """Display information on a single role
    """
    return ctx.gi.roles.show_role(role_id)
