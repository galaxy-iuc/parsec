import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_repositories')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get a list of all the repositories in a Galaxy Tool Shed.

Output:

    Returns a list of dictionaries containing information about
          repositories present in the Tool Shed.
          For example::

            [{u'category_ids': [u'c1df3132f6334b0e', u'f6d7b0037d901d9b'],
              u'deleted': False,
              u'deprecated': False,
              u'description': u'Order Contigs',
              u'homepage_url': u'',
              u'id': u'287bd69f724b99ce',
              u'name': u'best_tool_ever',
              u'owner': u'billybob',
              u'private': False,
              u'remote_repository_url': u'',
              u'times_downloaded': 0,
              u'type': u'unrestricted',
              u'url': u'/api/repositories/287bd69f724b99ce',
              u'user_id': u'5cefd48bc04af6d4'}]

        .. versionchanged:: 0.4.1
          Changed method name from ``get_tools`` to ``get_repositories`` to
          better align with the Tool Shed concepts.
    """
    return ctx.gi.repositories.get_repositories()
