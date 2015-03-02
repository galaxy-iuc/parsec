import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('workflows_export_workflow_to_local_path')
@options.galaxy_instance()
@click.argument("workflow_id", type=str)
@click.argument("file_local_path", type=str)

@click.option(
    "--use_default_filename",
    help="If the use_default_name parameter is True, the exported file will be saved as file_local_path/Galaxy-Workflow-%s.ga, where %s is the workflow name. If use_default_name is False, file_local_path is assumed to contain the full file path including filename.",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, workflow_id, file_local_path, use_default_filename=True):
    """Exports a workflow to a given local path.
    """
    return ctx.gi.workflows.export_workflow_to_local_path(workflow_id, file_local_path, use_default_filename=use_default_filename)