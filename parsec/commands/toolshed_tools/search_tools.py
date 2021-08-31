import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


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
@json_output
def cli(ctx, q, page=1, page_size=10):
    """Search for tools in a Galaxy Tool Shed.

Output:

    dictionary containing search hits as well as metadata for the
          search. For example::

            {'hits': [{'matched_terms': [],
                       'score': 3.0,
                       'tool': {'description': 'convert between various FASTQ quality formats',
                                'id': '69819b84d55f521efda001e0926e7233',
                                'name': 'FASTQ Groomer',
                                'repo_name': None,
                                'repo_owner_username': 'devteam'}},
                      {'matched_terms': [],
                       'score': 3.0,
                       'tool': {'description': 'converts a bam file to fastq files.',
                                'id': '521e282770fd94537daff87adad2551b',
                                'name': 'Defuse BamFastq',
                                'repo_name': None,
                                'repo_owner_username': 'jjohnson'}}],
             'hostname': 'https://testtoolshed.g2.bx.psu.edu/',
             'page': '1',
             'page_size': '2',
             'total_results': '118'}
    """
    return ctx.ti.tools.search_tools(q, page=page, page_size=page_size)
