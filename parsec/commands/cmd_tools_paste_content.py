import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_paste_content')
@options.galaxy_instance()
@click.argument("content", type=str)
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, content, history_id):
    """Upload a string to a new dataset in the history specified by ``history_id``.
    """
    return ctx.gi.tools.paste_content(content, history_id)
