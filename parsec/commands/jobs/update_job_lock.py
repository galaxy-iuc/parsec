import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, bool_output


@click.command('update_job_lock')
@click.option(
    "--active",
    help=""
)
@pass_context
@custom_exception
@bool_output
def cli(ctx, active=False):
    """Update the job lock status by setting ``active`` to either ``True`` or ``False``. If ``True``, all job dispatching will be blocked.

Output:

    Updated status of the job lock

        .. note::
          This method is only supported by Galaxy 20.05 or later and requires
          the user to be an admin.
    """
    return ctx.gi.jobs.update_job_lock(active=active)
