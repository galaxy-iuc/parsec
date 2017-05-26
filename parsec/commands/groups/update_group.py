import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('update_group')
@click.argument("group_id", type=str)

@click.option(
    "--group_name",
    help="A new name for the group. If None, the group name is not changed.",
    type=str
)
@click.option(
    "--user_ids",
    help="New list of encoded user IDs for the group. It will substitute the previous list of users (with [] if not specified)",
    type=str,
    multiple=True
)
@click.option(
    "--role_ids",
    help="New list of encoded role IDs for the group. It will substitute the previous list of roles (with [] if not specified)",
    type=str,
    multiple=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group_id, group_name="", user_ids=None, role_ids=None):
    """Update a group.
    """
    return ctx.gi.groups.update_group(group_id, group_name=group_name, user_ids=user_ids, role_ids=role_ids)
