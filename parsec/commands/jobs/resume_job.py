import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('resume_job')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id):
    """Resume a job if it is paused.

Output:

    dict containing output dataset associations

        .. note::
          This method is only supported by Galaxy 18.09 or later.
    """
    return ctx.gi.jobs.resume_job(job_id)
