import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('search_tools')
@click.argument("q", type=str)
@click.option(
    "--page",
    help="page requested",
    default="1",
    show_default=True,
    type=int
)
@click.option(
    "--page_size",
    help="page size requested",
    default="10",
    show_default=True,
    type=int
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, q, page=1, page_size=10):
    """Search for tools in a Galaxy Tool Shed.

Output:

    dictionary containing search hits as well as metadata for the
          search. For example::

            {u'hits': [{u'matched_terms': [],
               u'score': 3.0,
               u'tool': {u'description': u'convert between various FASTQ quality formats',
                u'id': u'69819b84d55f521efda001e0926e7233',
                u'name': u'FASTQ Groomer',
                u'repo_name': None,
                u'repo_owner_username': u'devteam'}},
              {u'matched_terms': [],
               u'score': 3.0,
               u'tool': {u'description': u'converts a bam file to fastq files.',
                u'id': u'521e282770fd94537daff87adad2551b',
                u'name': u'Defuse BamFastq',
                u'repo_name': None,
                u'repo_owner_username': u'jjohnson'}}],
             u'hostname': u'https://testtoolshed.g2.bx.psu.edu/',
             u'page': u'1',
             u'page_size': u'2',
             u'total_results': u'118'}
    """
    return ctx.gi.tools.search_tools(q, page=page, page_size=page_size)
