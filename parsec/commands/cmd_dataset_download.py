import click

from parsec.cli import pass_context
from parsec import options
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('dataset_download')
@options.galaxy_instance()

@click.argument('dataset_id')
@click.option(
    '--file_path',
    help='Where to download the file to, leave empty to use Galaxy history name',
)
@click.option(
    '--maxwait',
    default=12000,
    help='Maximum amount of time to wait for a dataset to download'
)
@pass_context
@dict_output
@bioblend_exception
def cli(ctx, galaxy_instance, dataset_id, file_path=None,
        wait_for_completion=True, maxwait=12000):
    """Download a dataset from Galaxy
    """
    gi = get_galaxy_instance(galaxy_instance)

    kwargs = {
        'file_path': '.',
        'use_default_filename': True,
        'wait_for_completion': True,
        'maxwait': maxwait
    }

    if file_path is not None:
        kwargs['use_default_filename'] = False
        kwargs['file_path'] = file_path

    return gi.dataset.download_dataset(dataset_id, **kwargs)
