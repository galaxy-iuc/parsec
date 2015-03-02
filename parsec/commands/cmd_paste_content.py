
import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('paste_content')
@options.galaxy_instance()

@click.argument("content", type=str)
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, content, history_id):
    """Upload a string to a new dataset in the history specified by ``history_id``.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tools.paste_content(content, history_id)
