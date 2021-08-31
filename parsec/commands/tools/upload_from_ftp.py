import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('upload_from_ftp')
@click.argument("path", type=str, help="path of the file in the user's FTP directory")
@click.argument("history_id", type=str, help="id of the history where to upload the file")
@pass_context
@custom_exception
@json_output
def cli(ctx, path, history_id):
    """Upload the file specified by ``path`` from the user's FTP directory to the history specified by ``history_id``.

Output:

    Information about the created upload job
    """
    return ctx.gi.tools.upload_from_ftp(path, history_id)
