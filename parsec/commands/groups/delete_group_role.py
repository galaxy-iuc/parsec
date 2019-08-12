import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('delete_group_role')
@click.argument("group_id", type=str)
@click.argument("role_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id, role_id):
    """Remove a role from the given group.

Output:

    The role which was removed
    """
    return ctx.gi.groups.delete_group_role(group_id, role_id)
