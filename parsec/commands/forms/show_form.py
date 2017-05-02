import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_form')
@click.argument("form_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, form_id):
    """Get details of a given form.
    """
    return ctx.gi.forms.show_form(form_id)
