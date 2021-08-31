import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('update_permissions')
@click.argument("dataset_id", type=str)
@click.option(
    "--access_ids",
    help="role IDs which should have access permissions for the dataset.",
    type=str,
    multiple=True
)
@click.option(
    "--manage_ids",
    help="role IDs which should have manage permissions for the dataset.",
    type=str,
    multiple=True
)
@click.option(
    "--modify_ids",
    help="role IDs which should have modify permissions for the dataset.",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_id, access_ids="", manage_ids="", modify_ids=""):
    """Set access, manage or modify permissions for a dataset to a list of roles.

Output:

    Current roles for all available permission types.

        .. note::
          This method can only be used with Galaxy ``release_19.05`` or later.
    """
    return ctx.gi.datasets.update_permissions(dataset_id, access_ids=access_ids, manage_ids=manage_ids, modify_ids=modify_ids)
