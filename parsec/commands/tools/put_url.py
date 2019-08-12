import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('put_url')
@click.argument("content", type=str)
@click.argument("history_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, content, history_id):
    """Upload a string to a new dataset in the history specified by ``history_id``.

Output:

    Information about the created upload job

        See :meth:`upload_file` for the optional parameters.
    """
    return ctx.gi.tools.put_url(content, history_id)
