import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('download_dataset')
@click.argument("history_id")
@click.argument("dataset_id")
@click.argument("file_path")

@click.option(
    "--use_default_filename",
    help="None"
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, dataset_id, file_path, use_default_filename=True):
    """Deprecated method, use :meth:`~bioblend.galaxy.datasets.DatasetClient.download_dataset` instead.
    """
    return ctx.gi.histories.download_dataset(history_id, dataset_id, file_path, use_default_filename=use_default_filename)
