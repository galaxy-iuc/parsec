import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_history_tag')
@click.argument("history_id", type=str)
@click.argument("tag", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, tag):
    """Create history tag
    """
    return ctx.gi.histories.create_history_tag(history_id, tag)
