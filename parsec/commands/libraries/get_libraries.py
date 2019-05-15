import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_libraries')
@click.option(
    "--library_id",
    help="filter for library by library id",
    type=str
)
@click.option(
    "--name",
    help="If ``name`` is set and multiple names match the given name, all the libraries matching the argument will be returned",
    type=str
)
@click.option(
    "--deleted",
    help="If ``False`` (the default), return only non-deleted libraries. If ``True``, return only deleted libraries. If ``None`, return both deleted and non-deleted libraries.",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, library_id="", name="", deleted=False):
    """Get all the libraries or filter for specific one(s) via the provided name or ID. Provide only one argument: ``name`` or ``library_id``, but not both.

Output:

    list of dicts each containing basic information about a library
    """
    return ctx.gi.libraries.get_libraries(library_id=library_id, name=name, deleted=deleted)
