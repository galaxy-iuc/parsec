import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_get_libraries')
@options.galaxy_instance()

@click.option(
    "--library_id",
    help="filter for library by library id",
    type=str
)
@click.option(
    "--name",
    help="If ``name`` is set and multiple names match the given name, all the libraries matching the argument will be returned.",
    type=str
)
@click.option(
    "--deleted",
    help="If set to ``True``, return libraries that have been deleted.",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id="", name="", deleted=False):
    """Get all the libraries or filter for specific one(s) via the provided name or ID. Provide only one argument: ``name`` or ``library_id``, but not both.
    """
    return ctx.gi.libraries.get_libraries(library_id=library_id, name=name, deleted=deleted)