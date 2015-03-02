import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries.show_dataset')
@options.galaxy_instance()

@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, library_id, dataset_id):
    """Get details about a given library dataset. The required ``library_id`` can be obtained from the datasets's library content details.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.show_dataset(library_id, dataset_id)

