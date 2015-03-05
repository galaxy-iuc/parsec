import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('groups_create_group')
@click.argument("group_name", type=str)
@click.option(
    "--user_ids",
    help="A list of encoded user IDs to add to the new group",
    type=str,
    multiple=True
)
@click.option(
    "--role_ids",
    help="A list of encoded role IDs to add to the new group",
    type=str,
    multiple=True
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group_name, user_ids=None, role_ids=None):
    """Create a new Galaxy group
    """
    return ctx.gi.groups.create_group(
        group_name,
        user_ids=user_ids,
        role_ids=role_ids)
