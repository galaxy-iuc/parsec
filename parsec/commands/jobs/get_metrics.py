import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_metrics')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id):
    """Return job metrics for a given job.

Output:

    list containing job metrics

        .. note::
          Calling ``show_job()`` with ``full_details=True`` also returns the
          metrics for a job if the user is an admin. This method allows to fetch
          metrics even as a normal user as long as the Galaxy instance has the
          ``expose_potentially_sensitive_job_metrics`` option set to ``true`` in
          the ``config/galaxy.yml`` configuration file.
    """
    return ctx.gi.jobs.get_metrics(job_id)
