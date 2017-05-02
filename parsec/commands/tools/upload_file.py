import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('upload_file')
@click.argument("path", type=str)
@click.argument("history_id", type=str)

@click.option(
    "--dbkey",
    help="(optional) genome dbkey",
    type=str
)
@click.option(
    "--to_posix_lines",
    help="if True, convert universal line endings to POSIX line endings. Default is True. Set to False if you upload a gzip, bz2 or zip archive containing a binary file",
    is_flag=True
)
@click.option(
    "--file_name",
    help="(optional) name of the new history dataset",
    type=str
)
@click.option(
    "--space_to_tab",
    help="whether to convert spaces to tabs. Default is False. Applicable only if to_posix_lines is True",
    is_flag=True
)
@click.option(
    "--file_type",
    help="Galaxy datatype for the new dataset, default is auto",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, path, history_id):
    """Upload the file specified by ``path`` to the history specified by ``history_id``.
    """
    kwargs = {}
    if dbkey and len(dbkey) > 0:
        kwargs['dbkey'] = dbkey
    if to_posix_lines is not None:
        kwargs['to_posix_lines'] = to_posix_lines
    if file_name and len(file_name) > 0:
        kwargs['file_name'] = file_name
    if space_to_tab is not None:
        kwargs['space_to_tab'] = space_to_tab
    if file_type and len(file_type) > 0:
        kwargs['file_type'] = file_type

    return ctx.gi.tools.upload_file(path, history_id, **kwargs)
