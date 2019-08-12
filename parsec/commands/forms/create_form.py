import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('create_form')
@click.argument("form_xml_text", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, form_xml_text):
    """Create a new form.

Output:

    Unique URL of newly created form with encoded id
    """
    return ctx.gi.forms.create_form(form_xml_text)
