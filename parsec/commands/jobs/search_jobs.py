import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('search_jobs')
@click.argument("job_info", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, job_info):
    """Return jobs for the current user based payload content.

Output:

    list of dictionaries containing summary job information of
          the jobs that match the requested job run

        This method is designed to scan the list of previously run jobs and find
        records of jobs that had the exact some input parameters and datasets.
        This can be used to minimize the amount of repeated work, and simply
        recycle the old results.
    """
    return ctx.gi.jobs.search_jobs(json_loads(job_info))
