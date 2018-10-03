import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('get_jobs')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Get the list of jobs of the current user.

Output:

    
    """
    return ctx.gi.jobs.get_jobs()
