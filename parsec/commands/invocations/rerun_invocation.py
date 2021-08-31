import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('rerun_invocation')
@click.argument("invocation_id", type=str)
@click.option(
    "--inputs_update",
    help="If different datasets should be used to the original invocation, this should contain a mapping of workflow inputs to the new datasets and dataset collections.",
    type=str
)
@click.option(
    "--params_update",
    help="If different non-dataset tool parameters should be used to the original invocation, this should contain a mapping of the new parameter values.",
    type=str
)
@click.option(
    "--history_id",
    help="The encoded history ID where to store the workflow outputs. Alternatively, ``history_name`` may be specified to create a new history.",
    type=str
)
@click.option(
    "--history_name",
    help="Create a new history with the given name to store the workflow outputs. If both ``history_id`` and ``history_name`` are provided, ``history_name`` is ignored. If neither is specified, a new 'Unnamed history' is created.",
    type=str
)
@click.option(
    "--import_inputs_to_history",
    help="If ``True``, used workflow inputs will be imported into the history. If ``False``, only workflow outputs will be visible in the given history.",
    is_flag=True
)
@click.option(
    "--replacement_params",
    help="pattern-based replacements for post-job actions",
    type=str
)
@click.option(
    "--allow_tool_state_corrections",
    help="If True, allow Galaxy to fill in missing tool state when running workflows. This may be useful for workflows using tools that have changed over time or for workflows built outside of Galaxy with only a subset of inputs defined.",
    is_flag=True
)
@click.option(
    "--inputs_by",
    help="Determines how inputs are referenced. Can be \"step_index|step_uuid\" (default), \"step_index\", \"step_id\", \"step_uuid\", or \"name\".",
    type=str
)
@click.option(
    "--parameters_normalized",
    help="Whether Galaxy should normalize the input parameters to ensure everything is referenced by a numeric step ID. Default is ``False``, but when setting parameters for a subworkflow, ``True`` is required.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id, inputs_update="", params_update="", history_id="", history_name="", import_inputs_to_history=False, replacement_params="", allow_tool_state_corrections=False, inputs_by="", parameters_normalized=False):
    """Rerun a workflow invocation. For more extensive documentation of all parameters, see the ``gi.workflows.invoke_workflow()`` method.

Output:

    A dict describing the new workflow invocation.

        .. note::
          This method can only be used with Galaxy ``release_21.01`` or later.
    """
    return ctx.gi.invocations.rerun_invocation(invocation_id, inputs_update=inputs_update, params_update=params_update, history_id=history_id, history_name=history_name, import_inputs_to_history=import_inputs_to_history, replacement_params=replacement_params, allow_tool_state_corrections=allow_tool_state_corrections, inputs_by=inputs_by, parameters_normalized=parameters_normalized)
