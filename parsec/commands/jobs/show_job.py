import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_job')
@click.argument("job_id", type=str)
@click.option(
    "--full_details",
    help="when ``True``, the complete list of details for the given job.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, job_id, full_details=False):
    """Get details of a given job of the current user.

Output:

    A description of the given job.
          For example::

            {'create_time': '2014-03-01T16:17:29.828624',
             'exit_code': 0,
             'id': 'a799d38679e985db',
             'inputs': {'input': {'id': 'ebfb8f50c6abde6d', 'src': 'hda'}},
             'model_class': 'Job',
             'outputs': {'output': {'id': 'a799d38679e985db', 'src': 'hda'}},
             'params': {'chromInfo': '"/opt/galaxy-central/tool-data/shared/ucsc/chrom/?.len"',
                        'dbkey': '"?"',
                        'seq_col': '"2"',
                        'title_col': '["1"]'},
             'state': 'ok',
             'tool_id': 'tab2fasta',
             'update_time': '2014-03-01T16:17:31.930728'}
    """
    return ctx.gi.jobs.show_job(job_id, full_details=full_details)
