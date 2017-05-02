import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_dataset')
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id, dataset_id):
    """Get details about a given library dataset. The required ``library_id`` can be obtained from the datasets's library content details.
    """
    return ctx.gi.libraries.show_dataset(library_id, dataset_id)
