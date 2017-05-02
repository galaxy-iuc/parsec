import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_job')
@click.argument("job_id", type=str)

@click.option(
    "--full_details",
    help="when ``True``, the complete list of details for the given job.",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_id, full_details=False):
    """Get details of a given job of the current user.
    """
    return ctx.gi.jobs.show_job(job_id, full_details=full_details)
