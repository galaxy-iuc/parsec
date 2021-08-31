import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('repository_revisions')
@click.option(
    "--downloadable",
    help="Can the tool be downloaded",
    is_flag=True
)
@click.option(
    "--malicious",
    help="",
    is_flag=True
)
@click.option(
    "--tools_functionally_correct",
    help="",
    is_flag=True
)
@click.option(
    "--missing_test_components",
    help="",
    is_flag=True
)
@click.option(
    "--do_not_test",
    help="",
    is_flag=True
)
@click.option(
    "--includes_tools",
    help="",
    is_flag=True
)
@click.option(
    "--test_install_error",
    help="",
    is_flag=True
)
@click.option(
    "--skip_tool_test",
    help="",
    is_flag=True
)
@pass_context
@custom_exception
@text_output
def cli(ctx, downloadable="", malicious="", tools_functionally_correct="", missing_test_components="", do_not_test="", includes_tools="", test_install_error="", skip_tool_test=""):
    """Returns a (possibly filtered) list of dictionaries that include information about all repository revisions. The following parameters can be used to filter the list.

Output:

    Returns a (possibly filtered) list of dictionaries that include
          information about all repository revisions.
          For example::

            [{'changeset_revision': '6e26c5a48e9a',
              'do_not_test': False,
              'downloadable': True,
              'has_repository_dependencies': False,
              'id': '92250afff777a169',
              'includes_datatypes': False,
              'includes_tool_dependencies': False,
              'includes_tools': True,
              'includes_tools_for_display_in_tool_panel': True,
              'includes_workflows': False,
              'malicious': False,
              'missing_test_components': False,
              'repository_id': '78f2604ff5e65707',
              'test_install_error': False,
              'time_last_tested': None,
              'tools_functionally_correct': False,
              'url': '/api/repository_revisions/92250afff777a169'},
             {'changeset_revision': '15a54fa11ad7',
              'do_not_test': False,
              'downloadable': True,
              'has_repository_dependencies': False,
              'id': 'd3823c748ae2205d',
              'includes_datatypes': False,
              'includes_tool_dependencies': False,
              'includes_tools': True,
              'includes_tools_for_display_in_tool_panel': True,
              'includes_workflows': False,
              'malicious': False,
              'missing_test_components': False,
              'repository_id': 'f9662009da7bfce0',
              'test_install_error': False,
              'time_last_tested': None,
              'tools_functionally_correct': False,
              'url': '/api/repository_revisions/d3823c748ae2205d'}]
    """
    return ctx.ti.repositories.repository_revisions(downloadable=downloadable, malicious=malicious, tools_functionally_correct=tools_functionally_correct, missing_test_components=missing_test_components, do_not_test=do_not_test, includes_tools=includes_tools, test_install_error=test_install_error, skip_tool_test=skip_tool_test)
