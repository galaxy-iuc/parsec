import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_group_users')
@click.argument("group_id", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, group_id):
    """Get the list of users associated to the given group.

Output:

    List of group users' info
    """
    return ctx.gi.groups.get_group_users(group_id)
