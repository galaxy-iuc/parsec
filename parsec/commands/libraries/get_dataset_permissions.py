import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_dataset_permissions')
@click.argument("dataset_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_id):
    """Get the permissions for a dataset.

Output:

    dictionary with all applicable permissions' values
    """
    return ctx.gi.libraries.get_dataset_permissions(dataset_id)
