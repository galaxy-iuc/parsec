import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('jobs_get_jobs')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of jobs for current user
    """
    return ctx.gi.jobs.get_jobs()
