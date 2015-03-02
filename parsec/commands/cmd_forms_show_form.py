import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('forms_show_form')
@options.galaxy_instance()

@click.argument("form_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, form_id):
    """Display information on a single form
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.forms.show_form(form_id)

