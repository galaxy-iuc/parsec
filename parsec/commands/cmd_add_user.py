import click

from parsec.cli import pass_context
from parsec import options
import bioblend


@click.command('add_user')
@options.optional_tools_arg()
@options.brew_option()
@pass_context
def cli(ctx, path, brew=None):
    """Add a user to a galaxy instance
    """
    for (tool_path, tool_xml) in load_tool_elements_from_path(path):
        ctx.log('Brewing requirements from tool %s',
                click.format_filename(tool_path))
        mock_args = bunch.Bunch(brew=brew)
        brew_context = brew_exts.BrewContext(mock_args)
        requirements, containers = parse_requirements_from_xml(tool_xml)

        for recipe_context in brew_util.requirements_to_recipe_contexts(
            requirements,
            brew_context
        ):
            brew_exts.versioned_install(recipe_context)
