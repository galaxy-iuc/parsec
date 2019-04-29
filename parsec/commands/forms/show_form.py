import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_form')
@click.argument("form_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, form_id):
    """Get details of a given form.

Output:

    A description of the given form.
          For example::

            {u'desc': u'here it is ',
             u'fields': [],
             u'form_definition_current_id': u'f2db41e1fa331b3e',
             u'id': u'f2db41e1fa331b3e',
             u'layout': [],
             u'model_class': u'FormDefinition',
             u'name': u'First form',
             u'url': u'/api/forms/f2db41e1fa331b3e'}
    """
    return ctx.gi.forms.show_form(form_id)
