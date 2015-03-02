
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_history')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("deleted", type=str)
@click.argument("visible", type=str)
@click.argument("details", type=str)
@click.argument("types", type=str)

@click.option(
    "--contents",
    help="When true, the complete list of datasets in the given history.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, deleted, visible, details, types, contents=False):
    """Get details of a given history. By default, just get the history meta information.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.show_history(history_id, deleted, visible, details, types, contents=contents)
