import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_outputs')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id):
    """Get dataset outputs produced by a job.

Output:

    Outputs of the given job
    """
    return ctx.gi.jobs.get_outputs(job_id)
