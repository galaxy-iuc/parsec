import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_repository')
@click.argument("toolShed_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, toolShed_id):
    """Get details of a given Tool Shed repository as it is installed on this Galaxy instance.

Output:

    Information about the tool
          For example::

            {'changeset_revision': 'b17455fb6222',
             'ctx_rev': '8',
             'owner': 'aaron',
             'status': 'Installed',
             'url': '/api/tool_shed_repositories/82de4a4c7135b20a'}

        .. versionchanged:: 0.4.1
            Changed method name from ``show_tool`` to ``show_repository`` to
            better align with the Tool Shed concepts
    """
    return ctx.gi.toolShed.show_repository(toolShed_id)
