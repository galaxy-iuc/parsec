import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('groups_show_group')
@options.galaxy_instance()

@click.argument("group_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, group_id):
    """Display information on a single group
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.groups.show_group(group_id)

