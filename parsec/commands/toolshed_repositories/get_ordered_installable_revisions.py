import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_ordered_installable_revisions')
@click.argument("name", type=str)
@click.argument("owner", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, name, owner):
    """Returns the ordered list of changeset revision hash strings that are associated with installable revisions. As in the changelog, the list is ordered oldest to newest.

Output:

    List of changeset revision hash strings from oldest to newest
    """
    return ctx.gi.repositories.get_ordered_installable_revisions(name, owner)
