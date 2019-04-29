import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_groups')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all (not deleted) groups.

Output:

    A list of dicts with details on individual groups.
          For example::

            [{'id': '33abac023ff186c2',
              'model_class': 'Group',
              'name': 'Listeria',
              'url': '/api/groups/33abac023ff186c2'},
             {'id': '73187219cd372cf8',
              'model_class': 'Group',
              'name': 'LPN',
              'url': '/api/groups/73187219cd372cf8'}]
    """
    return ctx.gi.groups.get_groups()
