import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_repository')
@click.argument("toolShed_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, toolShed_id):
    """Display information of a repository from Tool Shed

Output:

    Information about the tool.
          For example::

            {'category_ids': ['c1df3132f6334b0e', 'f6d7b0037d901d9b'],
             'deleted': False,
             'deprecated': False,
             'description': 'Order Contigs',
             'homepage_url': '',
             'id': '287bd69f724b99ce',
             'long_description': '',
             'name': 'best_tool_ever',
             'owner': 'billybob',
             'private': False,
             'remote_repository_url': '',
             'times_downloaded': 0,
             'type': 'unrestricted',
             'url': '/api/repositories/287bd69f724b99ce',
             'user_id': '5cefd48bc04af6d4'}

        .. versionchanged:: 0.4.1
          Changed method name from ``show_tool`` to ``show_repository`` to
          better align with the Tool Shed concepts.
    """
    return ctx.ti.repositories.show_repository(toolShed_id)
