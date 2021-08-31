import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('show_job_lock')
@pass_context
@custom_exception
@text_output
def cli(ctx):
    """Show whether the job lock is active or not. If it is active, no jobs will dispatch on the Galaxy server.

Output:

    Status of the job lock

        .. note::
          This method is only supported by Galaxy 20.05 or later and requires
          the user to be an admin.
    """
    return ctx.gi.jobs.show_job_lock()
