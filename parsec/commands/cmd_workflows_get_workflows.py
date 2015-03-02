import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_get_workflows')
@options.galaxy_instance()

@click.argument("name", type=str)
@click.argument("deleted", type=bool)

@click.option(
    "--workflow_id",
    help="Encoded workflow ID (incompatible with ``name``)",
    type=str
)
@click.option(
    "--published",
    help="If set to ``True``, return published workflows.",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, name, deleted, workflow_id=False, published=False):
    """Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.get_workflows(name, deleted, workflow_id=workflow_id, published=published)

