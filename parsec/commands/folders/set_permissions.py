import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('set_permissions')
@click.argument("folder_id", type=str)

@click.option(
    "--action",
    help="action to execute, only \"set_permissions\" is supported.",
    default="set_permissions",
    type=str
)
@click.option(
    "--add_ids",
    help="list of role IDs which can add datasets to the folder",
    type=str,
    multiple=True
)
@click.option(
    "--manage_ids",
    help="list of role IDs which can manage datasets in the folder",
    type=str,
    multiple=True
)
@click.option(
    "--modify_ids",
    help="list of role IDs which can modify datasets in the folder",
    type=str,
    multiple=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, folder_id, action="set_permissions", add_ids="", manage_ids="", modify_ids=""):
    """Set the permissions of a folder.
    """
    return ctx.gi.folders.set_permissions(folder_id, action=action, add_ids=add_ids, manage_ids=manage_ids, modify_ids=modify_ids)
