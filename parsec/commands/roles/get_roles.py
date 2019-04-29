import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_roles')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Displays a collection (list) of roles.

Output:

    A list of dicts with details on individual roles.
          For example::

            [{"id": "f2db41e1fa331b3e",
              "model_class": "Role",
              "name": "Foo",
              "url": "/api/roles/f2db41e1fa331b3e"},
             {"id": "f597429621d6eb2b",
              "model_class": "Role",
              "name": "Bar",
              "url": "/api/roles/f597429621d6eb2b"}]
    """
    return ctx.gi.roles.get_roles()
