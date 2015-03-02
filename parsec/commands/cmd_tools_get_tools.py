import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_get_tools')
@options.galaxy_instance()

@click.argument("tool_id", type=str)
@click.argument("name", type=str)
@click.argument("trackster")


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, tool_id, name, trackster):
    """Get all tools or filter the specific one(s) via the provided ``name`` or ``tool_id``. Provide only one argument, ``name`` or ``tool_id``, but not both.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tools.get_tools(tool_id, name, trackster)

