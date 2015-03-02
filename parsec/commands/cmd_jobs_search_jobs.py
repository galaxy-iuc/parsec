import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('jobs_search_jobs')
@options.galaxy_instance()

@click.argument("job_info", type=dict)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, job_info):
    """Return jobs for current user based payload content
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.jobs.search_jobs(job_info)

