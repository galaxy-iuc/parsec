import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('get_jobs')


@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Get the list of jobs of the current user.

Output:

    
    """
    return ctx.gi.jobs.get_jobs()
