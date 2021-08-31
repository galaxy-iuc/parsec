import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('update_repository')
@click.argument("id", type=str, help="Encoded repository ID")
@click.argument("tar_ball_path", type=str, help="Path to file containing tar ball to upload.")
@click.option(
    "--commit_message",
    help="Commit message used for the underlying Mercurial repository backing Tool Shed repository.",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, id, tar_ball_path, commit_message=""):
    """Update the contents of a Tool Shed repository with specified tar ball.

Output:

    Returns a dictionary that includes repository content warnings.
          Most valid uploads will result in no such warning and an exception
          will be raised generally if there are problems.
          For example a successful upload will look like::

            {'content_alert': '',
             'message': ''}

        .. versionadded:: 0.5.2
    """
    return ctx.ti.repositories.update_repository(id, tar_ball_path, commit_message=commit_message)
