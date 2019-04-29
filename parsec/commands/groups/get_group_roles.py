import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_group_roles')
@click.argument("group_id", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, group_id):
    """Get the list of roles associated to the given group.

Output:

    List of group roles' info
    """
    return ctx.gi.groups.get_group_roles(group_id)
