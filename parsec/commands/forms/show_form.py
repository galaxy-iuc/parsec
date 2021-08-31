import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_form')
@click.argument("form_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, form_id):
    """Get details of a given form.

Output:

    A description of the given form.
          For example::

            {'desc': 'here it is ',
             'fields': [],
             'form_definition_current_id': 'f2db41e1fa331b3e',
             'id': 'f2db41e1fa331b3e',
             'layout': [],
             'model_class': 'FormDefinition',
             'name': 'First form',
             'url': '/api/forms/f2db41e1fa331b3e'}
    """
    return ctx.gi.forms.show_form(form_id)
