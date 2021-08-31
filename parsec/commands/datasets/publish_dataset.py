import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('publish_dataset')
@click.argument("dataset_id", type=str)
@click.option(
    "--published",
    help="Whether to make the dataset published (``True``) or private (``False``).",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, dataset_id, published=False):
    """Make a dataset publicly available or private. For more fine-grained control (assigning different permissions to specific roles), use the ``update_permissions()`` method.

Output:

    Current roles for all available permission types.

        .. note::
          This method can only be used with Galaxy ``release_19.05`` or later.
    """
    return ctx.gi.datasets.publish_dataset(dataset_id, published=published)
