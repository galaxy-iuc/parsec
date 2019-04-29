import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_role')
@click.argument("role_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, role_id):
    """Display information on a single role

Output:

    A description of role
          For example::

            {"description": "Private Role for Foo",
             "id": "f2db41e1fa331b3e",
             "model_class": "Role",
             "name": "Foo",
             "type": "private",
             "url": "/api/roles/f2db41e1fa331b3e"}
    """
    return ctx.gi.roles.show_role(role_id)
