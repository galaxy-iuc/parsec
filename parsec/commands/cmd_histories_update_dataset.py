import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_update_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, dataset_id):
    """Update history dataset metadata. Some of the attributes that can be modified are documented below.
    """
    return ctx.gi.histories.update_dataset(history_id, dataset_id)
