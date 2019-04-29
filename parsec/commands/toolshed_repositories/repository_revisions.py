import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('repository_revisions')
@click.option(
    "--downloadable",
    help="Can the tool be downloaded",
    is_flag=True
)
@click.option(
    "--malicious",
    help=""
)
@click.option(
    "--tools_functionally_correct",
    help=""
)
@click.option(
    "--missing_test_components",
    help=""
)
@click.option(
    "--do_not_test",
    help=""
)
@click.option(
    "--includes_tools",
    help=""
)
@click.option(
    "--test_install_error",
    help=""
)
@click.option(
    "--skip_tool_test",
    help=""
)
@pass_context
@custom_exception
@list_output
def cli(ctx, downloadable="", malicious="", tools_functionally_correct="", missing_test_components="", do_not_test="", includes_tools="", test_install_error="", skip_tool_test=""):
    """Returns a (possibly filtered) list of dictionaries that include information about all repository revisions. The following parameters can be used to filter the list.

Output:

    Returns a (possibly filtered) list of dictionaries that include
          information about all repository revisions.
          For example::

            [{u'changeset_revision': u'6e26c5a48e9a',
              u'do_not_test': False,
              u'downloadable': True,
              u'has_repository_dependencies': False,
              u'id': u'92250afff777a169',
              u'includes_datatypes': False,
              u'includes_tool_dependencies': False,
              u'includes_tools': True,
              u'includes_tools_for_display_in_tool_panel': True,
              u'includes_workflows': False,
              u'malicious': False,
              u'missing_test_components': False,
              u'repository_id': u'78f2604ff5e65707',
              u'test_install_error': False,
              u'time_last_tested': None,
              u'tools_functionally_correct': False,
              u'url': u'/api/repository_revisions/92250afff777a169'},
             {u'changeset_revision': u'15a54fa11ad7',
              u'do_not_test': False,
              u'downloadable': True,
              u'has_repository_dependencies': False,
              u'id': u'd3823c748ae2205d',
              u'includes_datatypes': False,
              u'includes_tool_dependencies': False,
              u'includes_tools': True,
              u'includes_tools_for_display_in_tool_panel': True,
              u'includes_workflows': False,
              u'malicious': False,
              u'missing_test_components': False,
              u'repository_id': u'f9662009da7bfce0',
              u'test_install_error': False,
              u'time_last_tested': None,
              u'tools_functionally_correct': False,
              u'url': u'/api/repository_revisions/d3823c748ae2205d'}]
    """
    return ctx.gi.repositories.repository_revisions(downloadable=downloadable, malicious=malicious, tools_functionally_correct=tools_functionally_correct, missing_test_components=missing_test_components, do_not_test=do_not_test, includes_tools=includes_tools, test_install_error=test_install_error, skip_tool_test=skip_tool_test)
