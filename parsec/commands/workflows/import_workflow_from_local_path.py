import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('import_workflow_from_local_path')
@click.argument("file_local_path", type=str)
@click.option(
    "--publish",
    help="if ``True`` the uploaded workflow will be published; otherwise it will be visible only by the user which uploads it (default)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, file_local_path, publish=False):
    """Imports a new workflow given the path to a file containing a previously exported workflow.

Output:

    Information about the imported workflow.
          For example::

            {u'name': 'Training: 16S rRNA sequencing with mothur: main tutorial',
             u'tags': [],
             u'deleted': false,
             u'latest_workflow_uuid': '368c6165-ccbe-4945-8a3c-d27982206d66',
             u'url': '/api/workflows/94bac0a90086bdcf',
             u'number_of_steps': 44,
             u'published': false,
             u'owner': 'jane-doe',
             u'model_class': 'StoredWorkflow',
             u'id': '94bac0a90086bdcf'}
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path, publish=publish)
