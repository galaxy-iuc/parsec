import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_repository')
@click.argument("toolShed_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, toolShed_id):
    """Get details of a given Tool Shed repository as it is installed on this Galaxy instance.

Output:

    Information about the tool
          For example::

            {u'changeset_revision': u'b17455fb6222',
             u'ctx_rev': u'8',
             u'owner': u'aaron',
             u'status': u'Installed',
             u'url': u'/api/tool_shed_repositories/82de4a4c7135b20a'}

        .. versionchanged:: 0.4.1
            Changed method name from ``show_tool`` to ``show_repository`` to
            better align with the Tool Shed concepts
    """
    return ctx.gi.toolshed.show_repository(toolShed_id)
