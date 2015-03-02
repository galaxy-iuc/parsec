import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_create_history_tag')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("tag", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, tag):
    """Create history tag
    """
    return ctx.gi.histories.create_history_tag(history_id, tag)
