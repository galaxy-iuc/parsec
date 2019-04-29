import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_repository_revision')
@click.argument("metadata_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, metadata_id):
    """Returns a dictionary that includes information about a specified repository revision.

Output:

    Returns a dictionary that includes information about a
          specified repository revision.
          For example::

            {u'changeset_revision': u'7602de1e7f32',
             u'do_not_test': False,
             u'downloadable': True,
             u'has_repository_dependencies': False,
             u'id': u'504be8aaa652c154',
             u'includes_datatypes': False,
             u'includes_tool_dependencies': False,
             u'includes_tools': True,
             u'includes_tools_for_display_in_tool_panel': True,
             u'includes_workflows': False,
             u'malicious': False,
             u'missing_test_components': True,
             u'repository_id': u'491b7a3fddf9366f',
             u'test_install_error': False,
             u'time_last_tested': None,
             u'tool_test_results': {u'missing_test_components': []},
             u'tools_functionally_correct': False,
             u'url': u'/api/repository_revisions/504be8aaa652c154'}
    """
    return ctx.gi.repositories.show_repository_revision(metadata_id)
