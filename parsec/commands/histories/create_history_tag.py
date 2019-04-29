import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_history_tag')
@click.argument("history_id", type=str)
@click.argument("tag", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, tag):
    """Create history tag

Output:

    A dictionary with information regarding the tag.
          For example::

            {'id': 'f792763bee8d277a',
             'model_class': 'HistoryTagAssociation',
             'user_tname': 'NGS_PE_RUN',
             'user_value': None}
    """
    return ctx.gi.histories.create_history_tag(history_id, tag)
