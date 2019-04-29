import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('create_role')
@click.argument("role_name", type=str)
@click.argument("description", type=str)
@click.option(
    "--user_ids",
    help="A list of encoded user IDs to add to the new role",
    type=str,
    multiple=True
)
@click.option(
    "--group_ids",
    help="A list of encoded group IDs to add to the new role",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, role_name, description, user_ids=None, group_ids=None):
    """Create a new role.

Output:

    A (size 1) list with newly created role
          details, like::

            [{u'description': u'desc',
              u'url': u'/api/roles/ebfb8f50c6abde6d',
              u'model_class': u'Role',
              u'type': u'admin',
              u'id': u'ebfb8f50c6abde6d',
              u'name': u'Foo'}]
    """
    return ctx.gi.roles.create_role(role_name, description, user_ids=user_ids, group_ids=group_ids)
