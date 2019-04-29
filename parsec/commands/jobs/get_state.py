import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('get_state')
@click.argument("job_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, job_id):
    """Display the current state for a given job of the current user.

Output:

    state of the given job among the following values: `new`,
          `queued`, `running`, `waiting`, `ok`. If the state cannot be
          retrieved, an empty string is returned.

        .. versionadded:: 0.5.3
    """
    return ctx.gi.jobs.get_state(job_id)
