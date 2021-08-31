import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


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
@json_output
def cli(ctx, role_name, description, user_ids="", group_ids=""):
    """Create a new role.

Output:

    Details of the newly created role.
          For example::

            {'description': 'desc',
             'url': '/api/roles/ebfb8f50c6abde6d',
             'model_class': 'Role',
             'type': 'admin',
             'id': 'ebfb8f50c6abde6d',
             'name': 'Foo'}

        .. versionchanged:: 0.15.0
            Changed the return value from a 1-element list to a dict.
    """
    return ctx.gi.roles.create_role(role_name, description, user_ids=user_ids, group_ids=group_ids)
