import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('export_history')
@click.argument("history_id", type=str)

@click.option(
    "--gzip",
    help="create .tar.gz archive if ``True``, else .tar",
    default="True",
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

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, gzip=True, include_hidden=False, include_deleted=False, wait=False):
    """Start a job to create an export archive for the given history.
    """
    return ctx.gi.histories.export_history(history_id, gzip=gzip, include_hidden=include_hidden, include_deleted=include_deleted, wait=wait)
