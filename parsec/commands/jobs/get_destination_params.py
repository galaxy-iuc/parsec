import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_destination_params')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id):
    """Get destination parameters for a job, describing the environment and location where the job is run.

Output:

    Destination parameters for the given job

        .. note::
          This method is only supported by Galaxy 20.05 or later and requires
          the user to be an admin.
    """
    return ctx.gi.jobs.get_destination_params(job_id)
