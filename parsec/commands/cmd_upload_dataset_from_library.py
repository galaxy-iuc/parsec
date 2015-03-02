import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories.upload_dataset_from_library')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("lib_dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, lib_dataset_id):
    """Upload a dataset into the history from a library. Requires the library dataset ID, which can be obtained from the library contents.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.upload_dataset_from_library(history_id, lib_dataset_id)

