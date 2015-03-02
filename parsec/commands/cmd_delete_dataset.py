import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories.delete_dataset')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, dataset_id):
    """Mark corresponding dataset as deleted.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.delete_dataset(history_id, dataset_id)

