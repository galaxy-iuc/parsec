import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('invoke_workflow')
@click.argument("workflow_id", type=str)

@click.option(
    "--inputs",
    help="A mapping of workflow inputs to datasets and dataset collections. The datasets source can be a LibraryDatasetDatasetAssociation (``ldda``), LibraryDataset (``ld``), HistoryDatasetAssociation (``hda``), or HistoryDatasetCollectionAssociation (``hdca``).",
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
@click.option(
    "--allow_tool_state_corrections",
    help="If True, allow Galaxy to fill in missing tool state when running workflows. This may be useful for workflows using tools that have changed over time or for workflows built outside of Galaxy with only a subset of inputs defined.",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, inputs="", params="", history_id="", history_name="", import_inputs_to_history=False, replacement_params="", allow_tool_state_corrections=""):
    """Invoke the workflow identified by ``workflow_id``. This will cause a workflow to be scheduled and return an object describing the workflow invocation.
    """
    return ctx.gi.workflows.invoke_workflow(workflow_id, inputs=inputs, params=params, history_id=history_id, history_name=history_name, import_inputs_to_history=import_inputs_to_history, replacement_params=replacement_params, allow_tool_state_corrections=allow_tool_state_corrections)
