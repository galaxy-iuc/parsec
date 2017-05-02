import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_jobs')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the list of jobs of the current user.
    """
    return ctx.gi.jobs.get_jobs()
