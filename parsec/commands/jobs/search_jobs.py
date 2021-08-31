import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('search_jobs')
@click.argument("tool_id", type=str)
@click.argument("inputs", type=str)
@click.option(
    "--state",
    help="only return jobs in this state",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, tool_id, inputs, state=""):
    """Return jobs matching input parameters.

Output:

    Summary information for each matching job

        This method is designed to scan the list of previously run jobs and find
        records of jobs with identical input parameters and datasets. This can
        be used to minimize the amount of repeated work by simply recycling the
        old results.

        .. versionchanged:: 0.16.0
          Replaced the ``job_info`` parameter with separate ``tool_id``,
          ``inputs`` and ``state``.

        .. note::
          This method is only supported by Galaxy 18.01 or later.
    """
    return ctx.gi.jobs.search_jobs(tool_id, inputs, state=state)
