import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_update_history')
@options.galaxy_instance()
@click.argument("history_id", type=str)
@click.argument("name", type=str)
@click.argument("annotation", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, history_id, name, annotation):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    return ctx.gi.histories.update_history(history_id, name, annotation)
