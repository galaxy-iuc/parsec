import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('uninstall_repository_revision')
@click.argument("name", type=str, help="The name of the repository")
@click.argument("owner", type=str, help="The owner of the repository")
@click.argument("changeset_revision", type=str, help="The revision of the repository to uninstall")
@click.argument("tool_shed_url", type=str, help="URL of the Tool Shed from which the repository was installed from (e.g., ``https://testtoolshed.g2.bx.psu.edu``)")
@click.option(
    "--remove_from_disk",
    help="whether to also remove the repository from disk (the default) or only deactivate it",
    default="True",
    show_default=True,
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, name, owner, changeset_revision, tool_shed_url, remove_from_disk=True):
    """Uninstalls a specified repository revision from this Galaxy instance.

Output:

    If successful, a dictionary with a message noting the removal
    """
    return ctx.gi.toolShed.uninstall_repository_revision(name, owner, changeset_revision, tool_shed_url, remove_from_disk=remove_from_disk)
