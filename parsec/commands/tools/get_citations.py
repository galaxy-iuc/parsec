import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_citations')
@click.argument("tool_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, tool_id):
    """Get BibTeX citations for a given tool ID.

Output:

    
    """
    return ctx.gi.tools.get_citations(tool_id)
