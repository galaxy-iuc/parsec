import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

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
