import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('forms_show_form')
@click.argument("form_id", type=str)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, form_id):
    """Display information on a single form
    """
    return ctx.gi.forms.show_form(form_id)
