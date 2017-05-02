import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('upload_from_ftp')
@click.argument("path", type=str)
@click.argument("history_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, path, history_id):
    """Upload the file specified by ``path`` from the user's FTP directory to the history specified by ``history_id``.
    """
    return ctx.gi.tools.upload_from_ftp(path, history_id)
