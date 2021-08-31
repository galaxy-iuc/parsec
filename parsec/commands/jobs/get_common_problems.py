import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_common_problems')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id):
    """Query inputs and jobs for common potential problems that might have resulted in job failure.

Output:

    dict containing potential problems

        .. note::
          This method is only supported by Galaxy 19.05 or later.
    """
    return ctx.gi.jobs.get_common_problems(job_id)
