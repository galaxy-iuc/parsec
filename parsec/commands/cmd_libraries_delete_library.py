import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_delete_library')
@options.galaxy_instance()
@click.argument("library_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id):
    """Delete a data library
    """
    return ctx.gi.libraries.delete_library(library_id)
