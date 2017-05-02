import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('tools_run_tool')
@click.argument("history_id", type=str)
@click.argument("tool_id", type=str)
@click.argument("tool_inputs", type=dict)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, tool_id, tool_inputs):
    """Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.
    """
    return ctx.gi.tools.run_tool(history_id, tool_id, tool_inputs)
