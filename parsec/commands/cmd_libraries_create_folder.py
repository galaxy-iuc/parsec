import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_create_folder')
@options.galaxy_instance()
@click.argument("library_id", type=str)
@click.argument("folder_name", type=str)
@click.argument("description", type=str)
@click.argument("base_folder_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, folder_name, description, base_folder_id):
    """Create a folder in a library.
    """
    return ctx.gi.libraries.create_folder(library_id, folder_name, description, base_folder_id)
