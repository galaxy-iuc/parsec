import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('report_error')
@click.argument("job_id", type=str)
@click.argument("dataset_id", type=str)
@click.argument("message", type=str)
@click.option(
    "--email",
    help="Email for error report submission. If not specified, the email associated with the Galaxy user account is used by default.",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id, dataset_id, message, email=""):
    """Report an error for a given job and dataset to the server administrators.

Output:

    dict containing job error reply

        .. note::
          This method is only supported by Galaxy 20.01 or later.
    """
    return ctx.gi.jobs.report_error(job_id, dataset_id, message, email=email)
