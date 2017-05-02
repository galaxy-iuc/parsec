import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('paste_content')
@click.argument("content", type=str)
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, content, history_id):
    """Upload a string to a new dataset in the history specified by ``history_id``.
    """
    return ctx.gi.tools.paste_content(content, history_id)
