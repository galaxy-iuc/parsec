import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('update_repository')
@click.argument("id", type=str)
@click.argument("tar_ball_path", type=str)
@click.option(
    "--commit_message",
    help="Commit message used for the underlying Mercurial repository backing Tool Shed repository.",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id, tar_ball_path, commit_message=""):
    """Update the contents of a Tool Shed repository with specified tar ball.

Output:

    Returns a dictionary that includes repository content warnings.
          Most valid uploads will result in no such warning and an exception
          will be raised generally if there are problems.
          For example a successful upload will look like::

            {u'content_alert': u'',
             u'message': u''}

        .. versionadded:: 0.5.2
    """
    return ctx.gi.repositories.update_repository(id, tar_ball_path, commit_message=commit_message)
