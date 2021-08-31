import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('update_job_lock')
@click.option(
    "--active",
    help="The state of the job lock, locked=True",
    is_flag=True
)
@pass_context
@custom_exception
@text_output
def cli(ctx, active=False):
    """Update the job lock status by setting ``active`` to either ``True`` or ``False``. If ``True``, all job dispatching will be blocked.

Output:

    
    """
    return ctx.gi.jobs.update_job_lock(active=active)
