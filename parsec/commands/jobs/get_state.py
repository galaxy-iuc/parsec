import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_state')
@click.argument("job_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, job_id):
    """Display the current state for a given job of the current user.
    """
    return ctx.gi.jobs.get_state(job_id)
