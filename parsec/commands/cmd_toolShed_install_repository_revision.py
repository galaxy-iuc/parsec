import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('toolShed_install_repository_revision')
@options.galaxy_instance()
@click.argument("tool_shed_url", type=str)
@click.argument("changeset_revision", type=str)
@click.argument("install_tool_dependencies", type=bool)
@click.argument("install_repository_dependencies", type=bool)
@click.argument("tool_panel_section_id", type=str)
@click.argument("new_tool_panel_section_label", type=str)

@click.option(
    "--name",
    help="The name of the repository that should be installed",
    type=str
)
@click.option(
    "--owner",
    help="The name of the repository owner",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, tool_shed_url, changeset_revision, install_tool_dependencies, install_repository_dependencies, tool_panel_section_id, new_tool_panel_section_label, name=False, owner=False):
    """Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed, use ``install_tool_dependencies`` or ``install_repository_dependencies``.
    """
    return ctx.gi.toolShed.install_repository_revision(tool_shed_url, changeset_revision, install_tool_dependencies, install_repository_dependencies, tool_panel_section_id, new_tool_panel_section_label, name=name, owner=owner)
