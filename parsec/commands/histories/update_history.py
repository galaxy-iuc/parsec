import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('histories_update_history')
@click.argument("history_id", type=str)
@click.option(
    "--name",
    help="Replace history name with the given string",
    type=str
)
@click.option(
    "--annotation",
    help="Replace history annotation with given string",
    type=str
)
@click.option(
    "--published",
    help="Change history published status",
    type=bool
)
@click.option(
    "--importable",
    help="Change history importable status",
    type=bool
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, history_id, name="", annotation="", published=False, importable=False):
    """Update history metadata information. Some of the attributes that can be modified are documented below.
    """
    kwargs = {}
    if name and len(name) > 0:
        kwargs['name'] = name
    if annotation and len(annotation) > 0:
        kwargs['annotation'] = annotation
    if published is not None:
        kwargs['published'] = published
    if importable is not None:
        kwargs['importable'] = importable

    return ctx.gi.histories.update_history(
        history_id,
        **kwargs
    )
