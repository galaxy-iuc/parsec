import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets.show_stderr')
@options.galaxy_instance()

@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, dataset_id):
    """Display stderr output of a dataset.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.datasets.show_stderr(dataset_id)

