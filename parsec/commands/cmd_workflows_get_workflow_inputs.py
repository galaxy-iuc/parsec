import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_get_workflow_inputs')
@options.galaxy_instance()

@click.argument("workflow_id", type=str)
@click.argument("label", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, workflow_id, label):
    """Get a list of workflow input IDs that match the given label. If no input matches the given label, an empty list is returned.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.get_workflow_inputs(workflow_id, label)

