import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_jobs')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of jobs of the current user.

Output:

    list of dictionaries containing summary job information.
          For example::

            [{u'create_time': u'2014-03-01T16:16:48.640550',
              u'exit_code': 0,
              u'id': u'ebfb8f50c6abde6d',
              u'model_class': u'Job',
              u'state': u'ok',
              u'tool_id': u'fasta2tab',
              u'update_time': u'2014-03-01T16:16:50.657399'},
             {u'create_time': u'2014-03-01T16:05:34.851246',
              u'exit_code': 0,
              u'id': u'1cd8e2f6b131e891',
              u'model_class': u'Job',
              u'state': u'ok',
              u'tool_id': u'upload1',
              u'update_time': u'2014-03-01T16:05:39.558458'}]
    """
    return ctx.gi.jobs.get_jobs()
