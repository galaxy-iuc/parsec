import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_repository')
@click.argument("name", type=str)
@click.argument("synopsis", type=str)
@click.option(
    "--description",
    help="Optional description of the repository",
    type=str
)
@click.option(
    "--type",
    help="type of the repository. One of \"unrestricted\", \"repository_suite_definition\", or \"tool_dependency_definition\"",
    default="unrestricted",
    show_default=True,
    type=str
)
@click.option(
    "--remote_repository_url",
    help="Remote URL (e.g. GitHub/Bitbucket repository)",
    type=str
)
@click.option(
    "--homepage_url",
    help="Upstream's homepage for the project",
    type=str
)
@click.option(
    "--category_ids",
    help="List of encoded category IDs",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, name, synopsis, description="", type="unrestricted", remote_repository_url="", homepage_url="", category_ids=""):
    """Create a new repository in a Tool Shed.

Output:

    a dictionary containing information about the new repository.
          For example::

            {"deleted": false,
             "deprecated": false,
             "description": "new_synopsis",
             "homepage_url": "https://github.com/galaxyproject/",
             "id": "8cf91205f2f737f4",
             "long_description": "this is some repository",
             "model_class": "Repository",
             "name": "new_repo_17",
             "owner": "qqqqqq",
             "private": false,
             "remote_repository_url": "https://github.com/galaxyproject/tools-devteam",
             "times_downloaded": 0,
             "type": "unrestricted",
             "user_id": "adb5f5c93f827949"}
    """
    return ctx.gi.repositories.create_repository(name, synopsis, description=description, type=type, remote_repository_url=remote_repository_url, homepage_url=homepage_url, category_ids=category_ids)
