import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('jobs_show_job')
@click.argument("job_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_id):
    """Display information on a single job from current user
    """
    return ctx.gi.jobs.show_job(job_id)
