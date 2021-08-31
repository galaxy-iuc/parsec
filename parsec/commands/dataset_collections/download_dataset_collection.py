import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('download_dataset_collection')
@click.argument("dataset_collection_id", type=str)
@click.argument("file_path", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_collection_id, file_path):
    """Download a history dataset collection as an archive.

Output:

    Information about the downloaded archive.

        .. note::
          This method downloads a ``zip`` archive for Galaxy 21.01 and later.
          For earlier versions of Galaxy this method downloads a ``tgz`` archive.
          This method is only supported by Galaxy 18.01 or later.
    """
    return ctx.gi.dataset_collections.download_dataset_collection(dataset_collection_id, file_path)
