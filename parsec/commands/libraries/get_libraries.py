import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_libraries')
@click.option(
    "--library_id",
    help="filter for library by library id",
    type=str
)
@click.option(
    "--name",
    help="Library name to filter on.",
    type=str
)
@click.option(
    "--deleted",
    help="If ``False`` (the default), return only non-deleted libraries. If ``True``, return only deleted libraries. If ``None``, return both deleted and non-deleted libraries.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, library_id="", name="", deleted=False):
    """Get all libraries, or select a subset by specifying optional arguments for filtering (e.g. a library name).

Output:

    list of dicts each containing basic information about a library
    """
    return ctx.gi.libraries.get_libraries(library_id=library_id, name=name, deleted=deleted)
