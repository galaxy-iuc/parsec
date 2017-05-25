import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('install_repository_revision')
@click.argument("tool_shed_url", type=str)
@click.argument("name", type=str)
@click.argument("owner", type=str)
@click.argument("changeset_revision", type=str)

@click.option(
    "--install_tool_dependencies",
    help="Whether or not to automatically handle tool dependencies (see https://galaxyproject.org/toolshed/tool-dependency-recipes/ for more details)",
    is_flag=True
)
@click.option(
    "--install_repository_dependencies",
    help="Whether or not to automatically handle repository dependencies (see https://galaxyproject.org/toolshed/defining-repository-dependencies/ for more details)",
    is_flag=True
)
@click.option(
    "--install_resolver_dependencies",
    help="Whether or not to automatically install resolver dependencies (e.g. conda). This parameter is silently ignored in Galaxy ``release_16.04`` and earlier.",
    is_flag=True
)
@click.option(
    "--tool_panel_section_id",
    help="The ID of the Galaxy tool panel section where the tool should be insterted under. Note that you should specify either this parameter or the ``new_tool_panel_section_label``. If both are specified, this one will take precedence.",
    type=str
)
@click.option(
    "--new_tool_panel_section_label",
    help="The name of a Galaxy tool panel section that should be created and the repository installed into.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, tool_shed_url, name, owner, changeset_revision, install_tool_dependencies=False, install_repository_dependencies=False, install_resolver_dependencies=False, tool_panel_section_id="", new_tool_panel_section_label=""):
    """Install a specified repository revision from a specified Tool Shed into this Galaxy instance. This example demonstrates installation of a repository that contains valid tools, loading them into a section of the Galaxy tool panel or creating a new tool panel section. You can choose if tool dependencies or repository dependencies should be installed through the Tool Shed, (use ``install_tool_dependencies`` or ``install_repository_dependencies``) or through a resolver that supports installing dependencies (use ``install_resolver_dependencies``). Note that any combination of the three dependency resolving variables is valid.
    """
    return ctx.gi.toolshed.install_repository_revision(tool_shed_url, name, owner, changeset_revision, install_tool_dependencies=install_tool_dependencies, install_repository_dependencies=install_repository_dependencies, install_resolver_dependencies=install_resolver_dependencies, tool_panel_section_id=tool_panel_section_id, new_tool_panel_section_label=new_tool_panel_section_label)
