import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_repositories')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of all installed Tool Shed repositories on this Galaxy instance.

Output:

    a list of dictionaries containing information about
          repositories present in the Tool Shed.
          For example::

            [{u'changeset_revision': u'4afe13ac23b6',
              u'deleted': False,
              u'dist_to_shed': False,
              u'error_message': u'',
              u'name': u'velvet_toolsuite',
              u'owner': u'edward-kirton',
              u'status': u'Installed'}]

        .. versionchanged:: 0.4.1
            Changed method name from ``get_tools`` to ``get_repositories`` to
            better align with the Tool Shed concepts

        .. seealso:: bioblend.galaxy.tools.get_tool_panel()
    """
    return ctx.gi.toolShed.get_repositories()
