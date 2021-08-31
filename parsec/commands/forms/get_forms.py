import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_forms')
@pass_context
@custom_exception
@json_output
def cli(ctx):
    """Get the list of all forms.

Output:

    Displays a collection (list) of forms.
          For example::

            [{'id': 'f2db41e1fa331b3e',
              'model_class': 'FormDefinition',
              'name': 'First form',
              'url': '/api/forms/f2db41e1fa331b3e'},
             {'id': 'ebfb8f50c6abde6d',
              'model_class': 'FormDefinition',
              'name': 'second form',
              'url': '/api/forms/ebfb8f50c6abde6d'}]
    """
    return ctx.gi.forms.get_forms()
