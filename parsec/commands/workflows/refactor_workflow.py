import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('refactor_workflow')
@click.argument("workflow_id", type=str, help="Encoded workflow ID")
@click.argument("actions", type=str, multiple=True, help="Actions to use for refactoring the workflow. The following actions are supported: update_step_label, update_step_position, update_output_label, update_name, update_annotation, update_license, update_creator, update_report, add_step, add_input, disconnect, connect, fill_defaults, fill_step_defaults, extract_input, extract_legacy_parameter, remove_unlabeled_workflow_outputs, upgrade_all_steps, upgrade_subworkflow, upgrade_tool.")
@click.option(
    "--dry_run",
    help="When true, perform a dry run where the existing workflow is preserved. The refactored workflow is returned in the output of the method, but not saved on the Galaxy server.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, actions, dry_run=False):
    """Refactor workflow with given actions.

Output:

    Dictionary containing logged messages for the executed actions
                 and the refactored workflow.
    """
    return ctx.gi.workflows.refactor_workflow(workflow_id, actions, dry_run=dry_run)
