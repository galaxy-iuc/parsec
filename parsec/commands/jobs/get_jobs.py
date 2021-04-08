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

            [{'create_time': '2014-03-01T16:16:48.640550',
              'exit_code': 0,
              'id': 'ebfb8f50c6abde6d',
              'model_class': 'Job',
              'state': 'ok',
              'tool_id': 'fasta2tab',
              'update_time': '2014-03-01T16:16:50.657399'},
             {'create_time': '2014-03-01T16:05:34.851246',
              'exit_code': 0,
              'id': '1cd8e2f6b131e891',
              'model_class': 'Job',
              'state': 'ok',
              'tool_id': 'upload1',
              'update_time': '2014-03-01T16:05:39.558458'}]
    """
    return ctx.gi.jobs.get_jobs()
