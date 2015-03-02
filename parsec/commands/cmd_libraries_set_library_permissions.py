import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_set_library_permissions')
@options.galaxy_instance()

@click.argument("library_id", type=str)
@click.argument("access_in", type=list)
@click.argument("modify_in", type=list)
@click.argument("add_in", type=list)
@click.argument("manage_in", type=list)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, library_id, access_in, modify_in, add_in, manage_in):
    """Sets the permissions for a library.  Note: it will override all security for this library even if you leave out a permission type.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.libraries.set_library_permissions(library_id, access_in, modify_in, add_in, manage_in)

