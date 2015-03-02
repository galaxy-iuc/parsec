import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories.update_history')
@options.galaxy_instance()

@click.argument("history_id", type=str)
@click.argument("name", type=str)
@click.argument("annotation", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, history_id, name, annotation):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.update_history(history_id, name, annotation)

