import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_show_dataset_provenance')
@options.galaxy_instance()

@click.argument("follow", type=bool)

@click.option(
    "--history_id",
    help="Encoded history ID",
    type=str
)
@click.option(
    "--dataset_id",
    help="Encoded dataset ID",
    type=str
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, follow, history_id=False, dataset_id=False):
    """Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.histories.show_dataset_provenance(follow, history_id=history_id, dataset_id=dataset_id)

