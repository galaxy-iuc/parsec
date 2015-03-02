import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_create_library')
@options.galaxy_instance()
@click.argument("name", type=str)
@click.argument("description", type=str)
@click.argument("synopsis", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, name, description, synopsis):
    """Create a data library with the properties defined in the arguments. Return a list of JSON dicts, looking like so::
    """
    return ctx.gi.libraries.create_library(name, description, synopsis)
