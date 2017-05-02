import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('forms_create_form')
@click.argument("form_xml_text", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, form_xml_text):
    """Create a new form
    """
    return ctx.gi.forms.create_form(form_xml_text)
