import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_delete_workflow')
@options.galaxy_instance()

@click.argument("workflow_id", type=str)


@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, workflow_id):
    """Delete a workflow identified by `workflow_id`.
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.delete_workflow(workflow_id)

