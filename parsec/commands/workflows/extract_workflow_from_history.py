import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('extract_workflow_from_history')
@click.argument("history_id", type=str)
@click.argument("workflow_name", type=str)
@click.option(
    "--job_ids",
    help="Optional list of job IDs to filter the jobs to extract from the history",
    type=str,
    multiple=True
)
@click.option(
    "--dataset_hids",
    help="Optional list of dataset hids corresponding to workflow inputs when extracting a workflow from history",
    type=str,
    multiple=True
)
@click.option(
    "--dataset_collection_hids",
    help="Optional list of dataset collection hids corresponding to workflow inputs when extracting a workflow from history",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, workflow_name, job_ids="", dataset_hids="", dataset_collection_hids=""):
    """Extract a workflow from a history.

Output:

    A description of the created workflow
    """
    return ctx.gi.workflows.extract_workflow_from_history(history_id, workflow_name, job_ids=job_ids, dataset_hids=dataset_hids, dataset_collection_hids=dataset_collection_hids)
