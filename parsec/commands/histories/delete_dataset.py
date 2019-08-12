import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, none_output


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
@none_output
def cli(ctx, history_id, dataset_id, purge=False):
    """Mark corresponding dataset as deleted.

Output:

    None
        .. note::
            For the purge option to work, the Galaxy instance must have the
            ``allow_user_dataset_purge`` option set to ``true`` in the
            ``config/galaxy.yml`` configuration file.

        .. warning::
            If you purge a dataset which has not been previously deleted,
            Galaxy from release_15.03 to release_17.01 does not set the
            ``deleted`` attribute of the dataset to ``True``, see
            https://github.com/galaxyproject/galaxy/issues/3548
    """
    return ctx.gi.histories.delete_dataset(history_id, dataset_id, purge=purge)
