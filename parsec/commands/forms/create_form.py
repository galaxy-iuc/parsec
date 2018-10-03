import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('create_form')
@click.argument("form_xml_text", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, form_xml_text):
    """Create a new form.

Output:

    
    """
    return ctx.gi.forms.create_form(form_xml_text)
