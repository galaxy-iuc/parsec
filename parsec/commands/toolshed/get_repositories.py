import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_repositories')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of all installed Tool Shed repositories on this Galaxy instance.
    """
    return ctx.gi.toolshed.get_repositories()
