import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('download_dataset')
@click.argument("dataset_id", type=str)
@click.option(
    "--file_path",
    help="If this argument is provided, the dataset will be streamed to disk at that path (should be a directory if ``use_default_filename=True``). If the file_path argument is not provided, the dataset content is loaded into memory and returned by the method (Memory consumption may be heavy as the entire file will be in memory).",
    type=str
)
@click.option(
    "--use_default_filename",
    help="If ``True``, the exported file will be saved as ``file_path/%s``, where ``%s`` is the dataset name. If ``False``, ``file_path`` is assumed to contain the full file path including the filename.",
    default="True",
    show_default=True,
    is_flag=True
)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the dataset state to become terminal. If the dataset state is not terminal within this time, a ``DatasetTimeoutException`` will be thrown.",
    default="12000",
    show_default=True,
    type=float
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, dataset_id, file_path="", use_default_filename=True, maxwait=12000):
    """Download a dataset to file or in memory. If the dataset state is not 'ok', a ``DatasetStateException`` will be thrown.

Output:

    If a ``file_path`` argument is not provided, returns a dict containing the file content.
                 Otherwise returns nothing.
    """
    return ctx.gi.datasets.download_dataset(dataset_id, file_path=file_path, use_default_filename=use_default_filename, maxwait=maxwait)
