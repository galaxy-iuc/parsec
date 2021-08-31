import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_ordered_installable_revisions')
@click.argument("name", type=str, help="the name of the repository")
@click.argument("owner", type=str, help="the owner of the repository")
@pass_context
@custom_exception
@json_output
def cli(ctx, name, owner):
    """Returns the ordered list of changeset revision hash strings that are associated with installable revisions. As in the changelog, the list is ordered oldest to newest.

Output:

    List of changeset revision hash strings from oldest to newest
    """
    return ctx.ti.repositories.get_ordered_installable_revisions(name, owner)
