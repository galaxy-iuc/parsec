import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('rerun_job')
@click.argument("job_id", type=str)
@click.option(
    "--remap",
    help="when ``True``, the job output(s) will be remapped onto the dataset(s) created by the original job; if other jobs were waiting for this job to finish successfully, they will be resumed using the new outputs of this tool run. When ``False``, new job output(s) will be created. Note that if Galaxy does not permit remapping for the job in question, specifying ``True`` will result in an error.",
    is_flag=True
)
@click.option(
    "--tool_inputs_update",
    help="dictionary specifying any changes which should be made to tool parameters for the rerun job.",
    type=str
)
@click.option(
    "--history_id",
    help="ID of the history in which the job should be executed; if not specified, the same history will be used as the original job run.",
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id, remap=False, tool_inputs_update="", history_id=""):
    """Rerun a job.

Output:

    Information about outputs and the rerun job

        .. note::
          This method can only be used with Galaxy ``release_21.01`` or later.
    """
    return ctx.gi.jobs.rerun_job(job_id, remap=remap, tool_inputs_update=tool_inputs_update, history_id=history_id)
