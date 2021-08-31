import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('delete_dataset')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--purge",
    help="if ``True``, also purge (permanently delete) the dataset",
    is_flag=True
)
@pass_context
@custom_exception
@text_output
def cli(ctx, history_id, dataset_id, purge=False):
    """Mark corresponding dataset as deleted.

Output:

    None

        .. note::
            For the purge option to work, the Galaxy instance must have the
            ``allow_user_dataset_purge`` option set to ``true`` in the
            ``config/galaxy.yml`` configuration file.
    """
    return ctx.gi.histories.delete_dataset(history_id, dataset_id, purge=purge)
