import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('jobs_get_state')
@options.galaxy_instance()

@click.argument("job_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, job_id):
    """Display the current state for a single job from current user.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.jobs.get_state(job_id)

