import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('wait_for_job')
@click.argument("job_id", type=str)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the job state to become terminal. If the job state is not terminal within this time, a ``TimeoutException`` will be raised.",
    default="12000",
    show_default=True,
    type=float
)
@click.option(
    "--interval",
    help="Time (in seconds) to wait between 2 consecutive checks.",
    default="3",
    show_default=True,
    type=float
)
@click.option(
    "--check",
    help="Whether to check if the job terminal state is 'ok'.",
    default="True",
    show_default=True,
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id, maxwait=12000, interval=3, check=True):
    """Wait until a job is in a terminal state.

Output:

    Details of the given job.
    """
    return ctx.gi.jobs.wait_for_job(job_id, maxwait=maxwait, interval=interval, check=check)
