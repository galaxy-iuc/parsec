import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_forms')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of all forms.

Output:

    Displays a collection (list) of forms.
          For example::

            [{u'id': u'f2db41e1fa331b3e',
              u'model_class': u'FormDefinition',
              u'name': u'First form',
              u'url': u'/api/forms/f2db41e1fa331b3e'},
             {u'id': u'ebfb8f50c6abde6d',
              u'model_class': u'FormDefinition',
              u'name': u'second form',
              u'url': u'/api/forms/ebfb8f50c6abde6d'}]
    """
    return ctx.gi.forms.get_forms()
