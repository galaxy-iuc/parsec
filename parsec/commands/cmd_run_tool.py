import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools.run_tool')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("tool_id", type=str)
@click.argument("tool_inputs", type=dict)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, tool_id, tool_inputs):
    """Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tools.run_tool(history_id, tool_id, tool_inputs)

