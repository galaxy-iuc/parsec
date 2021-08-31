import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_jobs')
@click.option(
    "--state",
    help="Job states to filter on."
)
@click.option(
    "--history_id",
    help="Encoded history ID to filter on.",
    type=str
)
@click.option(
    "--invocation_id",
    help="Encoded workflow invocation ID to filter on.",
    type=str
)
@click.option(
    "--tool_id",
    help="Tool IDs to filter on.",
    type=str,
    multiple=True
)
@click.option(
    "--workflow_id",
    help="Encoded workflow ID to filter on.",
    type=str
)
@click.option(
    "--user_id",
    help="Encoded user ID to filter on. Only admin users can access the jobs of other users.",
    type=str
)
@click.option(
    "--date_range_min",
    help="Mininum job update date (in YYYY-MM-DD format) to filter on.",
    type=str
)
@click.option(
    "--date_range_max",
    help="Maximum job update date (in YYYY-MM-DD format) to filter on.",
    type=str
)
@click.option(
    "--limit",
    help="Maximum number of jobs to return.",
    default="500",
    show_default=True,
    type=int
)
@click.option(
    "--offset",
    help="Return jobs starting from this specified position. For example, if ``limit`` is set to 100 and ``offset`` to 200, jobs 200-299 will be returned.",
    type=int
)
@click.option(
    "--user_details",
    help="If ``True`` and the user is an admin, add the user email to each returned job dictionary.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, state="", history_id="", invocation_id="", tool_id="", workflow_id="", user_id="", date_range_min="", date_range_max="", limit=500, offset=0, user_details=False):
    """Get all jobs, or select a subset by specifying optional arguments for filtering (e.g. a state).

Output:

    Summary information for each selected job.
          For example::

            [{'create_time': '2014-03-01T16:16:48.640550',
              'exit_code': 0,
              'id': 'ebfb8f50c6abde6d',
              'model_class': 'Job',
              'state': 'ok',
              'tool_id': 'fasta2tab',
              'update_time': '2014-03-01T16:16:50.657399'},
             {'create_time': '2014-03-01T16:05:34.851246',
              'exit_code': 0,
              'id': '1cd8e2f6b131e891',
              'model_class': 'Job',
              'state': 'ok',
              'tool_id': 'upload1',
              'update_time': '2014-03-01T16:05:39.558458'}]

        .. note::
          The following filtering options can only be used with Galaxy ``release_21.05`` or later:
            user_id, limit, offset, workflow_id, invocation_id
    """
    return ctx.gi.jobs.get_jobs(state=state, history_id=history_id, invocation_id=invocation_id, tool_id=tool_id, workflow_id=workflow_id, user_id=user_id, date_range_min=date_range_min, date_range_max=date_range_max, limit=limit, offset=offset, user_details=user_details)
