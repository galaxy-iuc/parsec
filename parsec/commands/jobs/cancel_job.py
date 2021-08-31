import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('cancel_job')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@text_output
def cli(ctx, job_id):
    """Cancel a job, deleting output datasets.

Output:

    ``True`` if the job was successfully cancelled, ``False`` if
          it was already in a terminal state before the cancellation.
    """
    return ctx.gi.jobs.cancel_job(job_id)
