import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('run_workflow')
@click.argument("workflow_id", type=str)

@click.option(
    "--dataset_map",
    help="A mapping of workflow inputs to datasets. The datasets source can be a LibraryDatasetDatasetAssociation (``ldda``), LibraryDataset (``ld``), or HistoryDatasetAssociation (``hda``). The map must be in the following format: ``{'<input>': {'id': <encoded dataset ID>, 'src': '[ldda, ld, hda]'}}`` (e.g. ``{'23': {'id': '29beef4fadeed09f', 'src': 'ld'}}``)",
    type=str
)
@click.option(
    "--params",
    help="A mapping of non-datasets tool parameters (see below)",
    type=str
)
@click.option(
    "--history_id",
    help="The encoded history ID where to store the workflow output. Alternatively, ``history_name`` may be specified to create a new history.",
    type=str
)
@click.option(
    "--history_name",
    help="Create a new history with the given name to store the workflow output. If both ``history_id`` and ``history_name`` are provided, ``history_name`` is ignored. If neither is specified, a new 'Unnamed history' is created.",
    type=str
)
@click.option(
    "--import_inputs_to_history",
    help="If ``True``, used workflow inputs will be imported into the history. If ``False``, only workflow outputs will be visible in the given history.",
    is_flag=True
)
@click.option(
    "--replacement_params",
    help="pattern-based replacements for post-job actions (see below)",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, dataset_map="", params="", history_id="", history_name="", import_inputs_to_history=False, replacement_params=""):
    """Run the workflow identified by ``workflow_id``.
    """
    return ctx.gi.workflows.run_workflow(workflow_id, dataset_map=dataset_map, params=params, history_id=history_id, history_name=history_name, import_inputs_to_history=import_inputs_to_history, replacement_params=replacement_params)
