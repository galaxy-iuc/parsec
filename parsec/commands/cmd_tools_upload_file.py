import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('tools_upload_file')
@options.galaxy_instance()
@click.argument("path", type=str)
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, path, history_id):
    """Upload file specified by ``path`` to the history specified by ``history_id``.
    """
    return ctx.gi.tools.upload_file(path, history_id)
