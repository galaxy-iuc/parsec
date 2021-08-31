import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_category')
@click.argument("category_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, category_id):
    """Get details of a given category.

Output:

    details of the given category
    """
    return ctx.ti.categories.show_category(category_id)
