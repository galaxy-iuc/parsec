import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('config_get_config')
@options.galaxy_instance()


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance):
    """Get a list of attributes about galaxy instance. More attributes will be present if user is an admin
    """
    return ctx.gi.config.get_config()
