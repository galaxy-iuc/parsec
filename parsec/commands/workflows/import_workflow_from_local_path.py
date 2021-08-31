import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('import_workflow_from_local_path')
@click.argument("file_local_path", type=str)
@click.option(
    "--publish",
    help="if ``True`` the uploaded workflow will be published; otherwise it will be visible only by the user which uploads it (default)",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, file_local_path, publish=False):
    """Imports a new workflow given the path to a file containing a previously exported workflow.

Output:

    Information about the imported workflow.
          For example::

            {'name': 'Training: 16S rRNA sequencing with mothur: main tutorial',
             'tags': [],
             'deleted': false,
             'latest_workflow_uuid': '368c6165-ccbe-4945-8a3c-d27982206d66',
             'url': '/api/workflows/94bac0a90086bdcf',
             'number_of_steps': 44,
             'published': false,
             'owner': 'jane-doe',
             'model_class': 'StoredWorkflow',
             'id': '94bac0a90086bdcf'}
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path, publish=publish)
