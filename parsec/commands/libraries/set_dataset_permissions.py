import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('set_dataset_permissions')
@click.argument("dataset_id", type=str)
@click.option(
    "--access_in",
    help="list of role ids",
    type=str,
    multiple=True
)
@click.option(
    "--modify_in",
    help="list of role ids",
    type=str,
    multiple=True
)
@click.option(
    "--manage_in",
    help="list of role ids",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_id, access_in="", modify_in="", manage_in=""):
    """Set the permissions for a dataset. Note: it will override all security for this dataset even if you leave out a permission type.

Output:

    dictionary with all applicable permissions' values
    """
    return ctx.gi.libraries.set_dataset_permissions(dataset_id, access_in=access_in, modify_in=modify_in, manage_in=manage_in)
