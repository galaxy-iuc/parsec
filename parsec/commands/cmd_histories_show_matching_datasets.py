import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_matching_datasets')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("name_filter", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, name_filter):
    """Get dataset details for matching datasets within a history.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.show_matching_datasets(history_id, name_filter)

