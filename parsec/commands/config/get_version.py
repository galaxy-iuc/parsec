import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_version')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get the current version of the Galaxy instance. This functionality is available since Galaxy ``release_15.03``.
    """
    return ctx.gi.config.get_version()
