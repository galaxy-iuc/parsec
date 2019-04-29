import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_repository')
@click.argument("toolShed_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, toolShed_id):
    """Display information of a repository from Tool Shed

Output:

    Information about the tool.
          For example::

            {u'category_ids': [u'c1df3132f6334b0e', u'f6d7b0037d901d9b'],
             u'deleted': False,
             u'deprecated': False,
             u'description': u'Order Contigs',
             u'homepage_url': u'',
             u'id': u'287bd69f724b99ce',
             u'long_description': u'',
             u'name': u'best_tool_ever',
             u'owner': u'billybob',
             u'private': False,
             u'remote_repository_url': u'',
             u'times_downloaded': 0,
             u'type': u'unrestricted',
             u'url': u'/api/repositories/287bd69f724b99ce',
             u'user_id': u'5cefd48bc04af6d4'}

        .. versionchanged:: 0.4.1
          Changed method name from ``show_tool`` to ``show_repository`` to
          better align with the Tool Shed concepts.
    """
    return ctx.gi.repositories.show_repository(toolShed_id)
