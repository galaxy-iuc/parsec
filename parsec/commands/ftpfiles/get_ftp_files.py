import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_ftp_files')

@click.option(
    "--deleted",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, deleted=False):
    """Get a list of local files.
    """
    return ctx.gi.ftpfiles.get_ftp_files(deleted=deleted)
