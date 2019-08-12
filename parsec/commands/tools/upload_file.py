import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('upload_file')
@click.argument("path", type=str)
@click.argument("history_id", type=str)
@click.option(
    "--dbkey",
    help="(optional) genome dbkey",
    type=str
)
@click.option(
    "--file_name",
    help="(optional) name of the new history dataset",
    type=str
)
@click.option(
    "--file_type",
    help="(optional) Galaxy datatype for the new dataset, default is auto",
    type=str
)
@click.option(
    "--space_to_tab",
    help="whether to convert spaces to tabs. Default is ``False``. Applicable only if to_posix_lines is ``True``",
    is_flag=True
)
@click.option(
    "--to_posix_lines",
    help="if ``True`` (the default), convert universal line endings to POSIX line endings. Set to ``False`` when uploading a gzip, bz2 or zip archive containing a binary file",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, path, history_id, dbkey=None, file_name=None, file_type=None, space_to_tab=None, to_posix_lines=None):
    """Upload the file specified by ``path`` to the history specified by ``history_id``.

Output:

    Information about the created upload job
    """
    kwargs = {}
    if dbkey and len(dbkey) > 0:
        kwargs['dbkey'] = dbkey
    if file_name and len(file_name) > 0:
        kwargs['file_name'] = file_name
    if file_type and len(file_type) > 0:
        kwargs['file_type'] = file_type
    if space_to_tab is not None:
        kwargs['space_to_tab'] = space_to_tab
    if to_posix_lines is not None:
        kwargs['to_posix_lines'] = to_posix_lines

    return ctx.gi.tools.upload_file(path, history_id, **kwargs)
