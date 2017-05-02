import click
import json
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('search_jobs')
@click.argument("job_info", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_info):
    """Return jobs for the current user based payload content.
    """
    return ctx.gi.jobs.search_jobs(job_info)
