import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_group_roles')
@click.argument("group_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group_id):
    """Get the list of roles associated to the given group.
    """
    return ctx.gi.groups.get_group_roles(group_id)
