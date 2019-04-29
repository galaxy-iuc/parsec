import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('delete_library_dataset')
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--purged",
    help="Indicate that the dataset should be purged (permanently deleted)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, library_id, dataset_id, purged=False):
    """Delete a library dataset in a data library.

Output:

    A dictionary containing the dataset id and whether the dataset
          has been deleted.
          For example::

            {u'deleted': True,
             u'id': u'60e680a037f41974'}
    """
    return ctx.gi.libraries.delete_library_dataset(library_id, dataset_id, purged=purged)
