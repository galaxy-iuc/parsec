import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_ftp_files')
@click.option(
    "--deleted",
    help="Whether to include deleted files",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, deleted=False):
    """Get a list of local files.

Output:

    A list of dicts with details on individual files on FTP
    """
    return ctx.gi.ftpfiles.get_ftp_files(deleted=deleted)
