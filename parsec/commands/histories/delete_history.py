import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('delete_history')
@click.argument("history_id", type=str)
@click.option(
    "--purge",
    help="if ``True``, also purge (permanently delete) the history",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, purge=False):
    """Delete a history.

Output:

    An error object if an error occurred or a dictionary
                 containing: ``id`` (the encoded id of the history), ``deleted`` (if the
                 history was marked as deleted), ``purged`` (if the history was
                 purged).

        .. note::
          For the purge option to work, the Galaxy instance must have the
          ``allow_user_dataset_purge`` option set to ``true`` in the
          ``config/galaxy.yml`` configuration file.
    """
    return ctx.gi.histories.delete_history(history_id, purge=purge)
