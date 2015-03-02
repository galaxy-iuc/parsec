import click

from parsec import options
from parsec.cli import pass_context
from parsec.io import info
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_run_workflow')
@options.galaxy_instance()

@click.argument("workflow_id", type=str)
@click.argument("dataset_map")
@click.argument("params")
@click.argument("history_id", type=str)
@click.argument("history_name", type=str)
@click.argument("replacement_params", type=dict)

@click.option(
    "--import_inputs_to_history",
    help="If ``True``, used workflow inputs will be imported into the history. If ``False``, only workflow outputs will be visible in the given history.",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output

def cli(ctx, galaxy_instance, workflow_id, dataset_map, params, history_id, history_name, replacement_params, import_inputs_to_history=False):
    """Run the workflow identified by ``workflow_id``
    """
    gi = get_galaxy_instance(galaxy_instance)

    return gi.workflows.run_workflow(workflow_id, dataset_map, params, history_id, history_name, replacement_params, import_inputs_to_history=import_inputs_to_history)

