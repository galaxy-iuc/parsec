import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_job')
@click.argument("job_id", type=str)
@click.option(
    "--full_details",
    help="when ``True``, the complete list of details for the given job.",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, job_id, full_details=False):
    """Get details of a given job of the current user.

Output:

    A description of the given job.
          For example::

            {u'create_time': u'2014-03-01T16:17:29.828624',
             u'exit_code': 0,
             u'id': u'a799d38679e985db',
             u'inputs': {u'input': {u'id': u'ebfb8f50c6abde6d',
               u'src': u'hda'}},
             u'model_class': u'Job',
             u'outputs': {u'output': {u'id': u'a799d38679e985db',
               u'src': u'hda'}},
             u'params': {u'chromInfo': u'"/opt/galaxy-central/tool-data/shared/ucsc/chrom/?.len"',
               u'dbkey': u'"?"',
               u'seq_col': u'"2"',
               u'title_col': u'["1"]'},
             u'state': u'ok',
             u'tool_id': u'tab2fasta',
             u'update_time': u'2014-03-01T16:17:31.930728'}
    """
    return ctx.gi.jobs.show_job(job_id, full_details=full_details)
