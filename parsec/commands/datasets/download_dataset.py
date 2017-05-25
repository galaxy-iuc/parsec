import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('download_dataset')
@click.argument("dataset_id", type=str)

@click.option(
    "--file_path",
    help="If this argument is provided, the dataset will be streamed to disk at that path (should be a directory if use_default_filename=True). If the file_path argument is not provided, the dataset content is loaded into memory and returned by the method (Memory consumption may be heavy as the entire file will be in memory).",
    type=str
)
@click.option(
    "--use_default_filename",
    help="If this argument is True, the exported file will be saved as file_path/%s, where %s is the dataset name. If this argument is False, file_path is assumed to contain the full file path including the filename.",
    default="True",
    is_flag=True
)
@click.option(
    "--wait_for_completion",
    help="If this argument is True, this method call will block until the dataset is ready. If the dataset state becomes invalid, a DatasetStateException will be thrown.",
    is_flag=True
)
@click.option(
    "--maxwait",
    help="Time (in seconds) to wait for dataset to complete. If the dataset state is not complete within this time, a DatasetTimeoutException will be thrown.",
    default="12000",
    type=float
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, dataset_id, file_path="", use_default_filename=True, wait_for_completion=False, maxwait=12000):
    """Download a dataset to file or in memory.
    """
    return ctx.gi.datasets.download_dataset(dataset_id, file_path=file_path, use_default_filename=use_default_filename, wait_for_completion=wait_for_completion, maxwait=maxwait)
