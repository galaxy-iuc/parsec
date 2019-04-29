import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_invocation')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id, invocation_id):
    """Get a workflow invocation object representing the scheduling of a workflow. This object may be sparse at first (missing inputs and invocation steps) and will become more populated as the workflow is actually scheduled.

Output:

    The workflow invocation.
          For example::

            {u'history_id': u'2f94e8ae9edff68a',
             u'id': u'df7a1f0c02a5b08e',
             u'inputs': {u'0': {u'id': u'a7db2fac67043c7e',
               u'src': u'hda',
               u'uuid': u'7932ffe0-2340-4952-8857-dbaa50f1f46a'}},
             u'model_class': u'WorkflowInvocation',
             u'state': u'ready',
             u'steps': [{u'action': None,
               u'id': u'd413a19dec13d11e',
               u'job_id': None,
               u'model_class': u'WorkflowInvocationStep',
               u'order_index': 0,
               u'state': None,
               u'update_time': u'2015-10-31T22:00:26',
               u'workflow_step_id': u'cbbbf59e8f08c98c',
               u'workflow_step_label': None,
               u'workflow_step_uuid': u'b81250fd-3278-4e6a-b269-56a1f01ef485'},
              {u'action': None,
               u'id': u'2f94e8ae9edff68a',
               u'job_id': u'e89067bb68bee7a0',
               u'model_class': u'WorkflowInvocationStep',
               u'order_index': 1,
               u'state': u'new',
               u'update_time': u'2015-10-31T22:00:26',
               u'workflow_step_id': u'964b37715ec9bd22',
               u'workflow_step_label': None,
               u'workflow_step_uuid': u'e62440b8-e911-408b-b124-e05435d3125e'}],
             u'update_time': u'2015-10-31T22:00:26',
             u'uuid': u'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
             u'workflow_id': u'03501d7626bd192f'}
    """
    return ctx.gi.workflows.show_invocation(workflow_id, invocation_id)
