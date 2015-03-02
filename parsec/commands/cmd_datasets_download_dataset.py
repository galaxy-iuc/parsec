import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('datasets_download_dataset')
@options.galaxy_instance()

@click.argument("dataset_id", type=str)
@click.argument("file_path", type=str)
@click.argument("file_ext", type=str)

@click.option(
    "--use_default_filename",
    help="If the use_default_name parameter is True, the exported file will be saved as file_path/%s, where %s is the dataset name. If use_default_name is False, file_path is assumed to contain the full file path including filename.",
    type=bool
)
@click.option(
    "--wait_for_completion",
    help="If wait_for_completion is True, this call will block until the dataset is ready. If the dataset state becomes invalid, a DatasetStateException will be thrown.",
    type=bool
)
@click.option(
    "--maxwait",
    help="Time (in seconds) to wait for dataset to complete. If the dataset state is not complete within this time, a DatasetTimeoutException will be thrown.",
    type=float
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, dataset_id, file_path, file_ext, use_default_filename=True, wait_for_completion=False, maxwait=12000):
    """Downloads the dataset identified by 'id'.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.datasets.download_dataset(dataset_id, file_path, file_ext, use_default_filename=use_default_filename, wait_for_completion=wait_for_completion, maxwait=maxwait)

