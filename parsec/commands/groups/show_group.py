import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_group')
@click.argument("group_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group_id):
    """Get details of a given group.
    """
    return ctx.gi.groups.show_group(group_id)
