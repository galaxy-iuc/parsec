import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
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
    gi = get_galaxy_instance(galaxy_instance)

    return gi.ftpfiles.get_ftp_files(deleted=deleted)

