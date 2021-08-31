import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_repository_revision')
@click.argument("metadata_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, metadata_id):
    """Returns a dictionary that includes information about a specified repository revision.

Output:

    Returns a dictionary that includes information about a
          specified repository revision.
          For example::

            {'changeset_revision': '7602de1e7f32',
             'do_not_test': False,
             'downloadable': True,
             'has_repository_dependencies': False,
             'id': '504be8aaa652c154',
             'includes_datatypes': False,
             'includes_tool_dependencies': False,
             'includes_tools': True,
             'includes_tools_for_display_in_tool_panel': True,
             'includes_workflows': False,
             'malicious': False,
             'missing_test_components': True,
             'repository_id': '491b7a3fddf9366f',
             'test_install_error': False,
             'time_last_tested': None,
             'tool_test_results': {'missing_test_components': []},
             'tools_functionally_correct': False,
             'url': '/api/repository_revisions/504be8aaa652c154'}
    """
    return ctx.ti.repositories.show_repository_revision(metadata_id)
