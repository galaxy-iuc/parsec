import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('create_group')
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
@custom_exception
@list_output
def cli(ctx, group_name, user_ids=None, role_ids=None):
    """Create a new group.

Output:

    A (size 1) list with newly created group
          details, like::

            [{u'id': u'7c9636938c3e83bf',
              u'model_class': u'Group',
              u'name': u'My Group Name',
              u'url': u'/api/groups/7c9636938c3e83bf'}]
    """
    return ctx.gi.groups.create_group(group_name, user_ids=user_ids, role_ids=role_ids)
