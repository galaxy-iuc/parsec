import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


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
@custom_exception
@dict_output
def cli(ctx, workflow_id, dataset_map="", params="", history_id="", history_name="", import_inputs_to_history=False, replacement_params=""):
    """Run the workflow identified by ``workflow_id``.

Output:

    A dict containing the history ID where the outputs are placed
          as well as output dataset IDs. For example::

            {u'history': u'64177123325c9cfd',
             u'outputs': [u'aa4d3084af404259']}

        The ``params`` dict should be specified as follows::

          {STEP_ID: PARAM_DICT, ...}

        where PARAM_DICT is::

          {PARAM_NAME: VALUE, ...}

        For backwards compatibility, the following (deprecated) format is
        also supported for ``params``::

          {TOOL_ID: PARAM_DICT, ...}

        in which case PARAM_DICT affects all steps with the given tool id.
        If both by-tool-id and by-step-id specifications are used, the
        latter takes precedence.

        Finally (again, for backwards compatibility), PARAM_DICT can also
        be specified as::

          {'param': PARAM_NAME, 'value': VALUE}

        Note that this format allows only one parameter to be set per step.

        The ``replacement_params`` dict should map parameter names in
        post-job actions (PJAs) to their runtime values. For
        instance, if the final step has a PJA like the following::

          {u'RenameDatasetActionout_file1': {u'action_arguments': {u'newname': u'${output}'},
            u'action_type': u'RenameDatasetAction',
            u'output_name': u'out_file1'}}

        then the following renames the output dataset to 'foo'::

          replacement_params = {'output': 'foo'}

        see also `this email thread
        <http://lists.bx.psu.edu/pipermail/galaxy-dev/2011-September/006875.html>`_.

        .. warning::
            This method waits for the whole workflow to be scheduled before
            returning and does not scale to large workflows as a result. This
            method has therefore been deprecated in favor of
            :meth:`invoke_workflow`, which also features improved default
            behavior for dataset input handling.
    """
    return ctx.gi.workflows.run_workflow(workflow_id, dataset_map=dataset_map, params=params, history_id=history_id, history_name=history_name, import_inputs_to_history=import_inputs_to_history, replacement_params=replacement_params)
