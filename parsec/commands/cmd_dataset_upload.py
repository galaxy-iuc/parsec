import click

from parsec.cli import pass_context
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('dataset_upload')
@options.galaxy_instance()

@click.argument('path', type=click.Path(exists=True))
@click.argument('history_id')
@click.option(
    '--file_name',
    help='Name of the new history dataset',
)
@click.option(
    '--file_type',
    help='Galaxy datatype for the new dataset',
    default='auto'
)
@click.option(
    '--dbkey',
    help='Genome dbkey',
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, path, history_id, file_name=None, file_type="auto", dbkey=None):
    """Upload a dataset to a Galaxy history
    """
    # TODO, find better way of passing args around
    gi = get_galaxy_instance(galaxy_instance)

    return gi.tools.upload_file(path, history_id, file_name=file_name,
                                file_type=file_type, dbkey=dbkey)
