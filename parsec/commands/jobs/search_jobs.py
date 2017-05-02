import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('search_jobs')
@click.argument("job_info", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_info):
    """Return jobs for the current user based payload content.
    """
    return ctx.gi.jobs.search_jobs(json_loads(job_info))
