import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('report_error')
@click.argument("job_id", type=str)
@click.argument("dataset_id", type=str)
@click.argument("message", type=str)
@click.option(
    "--email",
    help="Email to submit error report to",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, job_id, dataset_id, message, email=""):
    """Report an error for a given job and dataset.

Output:

    dict containing job error reply
    """
    return ctx.gi.jobs.report_error(job_id, dataset_id, message, email=email)
