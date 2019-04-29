import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_group')
@click.argument("group_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id):
    """Get details of a given group.

Output:

    A description of group
          For example::

            {'id': '33abac023ff186c2',
             'model_class': 'Group',
             'name': 'Listeria',
             'roles_url': '/api/groups/33abac023ff186c2/roles',
             'url': '/api/groups/33abac023ff186c2',
             'users_url': '/api/groups/33abac023ff186c2/users'}
    """
    return ctx.gi.groups.show_group(group_id)
