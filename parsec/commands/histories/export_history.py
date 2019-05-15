import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('export_history')
@click.argument("history_id", type=str)
@click.option(
    "--gzip",
    help="create .tar.gz archive if ``True``, else .tar",
    default="True",
    show_default=True,
    is_flag=True
)
@click.option(
    "--include_hidden",
    help="whether to include hidden datasets in the export",
    is_flag=True
)
@click.option(
    "--include_deleted",
    help="whether to include deleted datasets in the export",
    is_flag=True
)
@click.option(
    "--wait",
    help="if ``True``, block until the export is ready; else, return immediately",
    is_flag=True
)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the export to become ready. When set, implies that ``wait`` is ``True``.",
    type=float
)
@pass_context
@custom_exception
@str_output
def cli(ctx, history_id, gzip=True, include_hidden=False, include_deleted=False, wait=False, maxwait=""):
    """Start a job to create an export archive for the given history.

Output:

    ``jeha_id`` of the export, or empty if ``wait`` is ``False``
          and the export is not ready.
    """
    return ctx.gi.histories.export_history(history_id, gzip=gzip, include_hidden=include_hidden, include_deleted=include_deleted, wait=wait, maxwait=maxwait)
