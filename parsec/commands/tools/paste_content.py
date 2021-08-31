import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('paste_content')
@click.argument("content", type=str, help="content of the new dataset to upload or a list of URLs (one per line) to upload")
@click.argument("history_id", type=str, help="id of the history where to upload the content")
@pass_context
@custom_exception
@json_output
def cli(ctx, content, history_id):
    """Upload a string to a new dataset in the history specified by ``history_id``.

Output:

    Information about the created upload job

        See :meth:`upload_file` for the optional parameters.
    """
    return ctx.gi.tools.paste_content(content, history_id)
