
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_dataset_collection')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("dataset_collection_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, dataset_collection_id):
    """Get details about a given history dataset collection.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.show_dataset_collection(history_id, dataset_collection_id)
