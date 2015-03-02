import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('groups_create_group')
@options.galaxy_instance()

@click.option(
    "--group_name",
    help="A name for new group",
    type=str
)
@click.option(
    "--user_ids",
    help="A list of encoded user IDs to add to the new group",
    type=list
)
@click.option(
    "--role_ids",
    help="A list of encoded role IDs to add to the new group",
    type=list
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, group_name=[], user_ids=[], role_ids=[]):
    """Create a new Galaxy group
    """
    return ctx.gi.groups.create_group(group_name=group_name, user_ids=user_ids, role_ids=role_ids)
