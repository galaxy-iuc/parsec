import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('forms_get_forms')
@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of forms
    """
    return ctx.gi.forms.get_forms()
