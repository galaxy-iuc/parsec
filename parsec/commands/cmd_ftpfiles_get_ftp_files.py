import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('ftpfiles_get_ftp_files')
@options.galaxy_instance()

@click.option(
    "--deleted",
    help="None"
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, deleted=False):
    """Get a list of local files
    """
    return ctx.gi.ftpfiles.get_ftp_files(deleted=deleted)
