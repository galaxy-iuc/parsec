import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('jobs_get_state')
@click.argument("job_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_id):
    """Display the current state for a single job from current user.
    """
    return ctx.gi.jobs.get_state(job_id)
