import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('search_repositories')
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
    """Search for repositories in a Galaxy Tool Shed.

Output:

    dictionary containing search hits as well as metadata for the
          search.
          For example::

            {'hits': [{'matched_terms': [],
                       'repository': {'approved': 'no',
                                      'description': 'Convert export file to fastq',
                                      'full_last_updated': '2015-01-18 09:48 AM',
                                      'homepage_url': '',
                                      'id': 'bdfa208f0cf6504e',
                                      'last_updated': 'less than a year',
                                      'long_description': 'This is a simple too to convert Solexas Export files to FASTQ files.',
                                      'name': 'export_to_fastq',
                                      'remote_repository_url': '',
                                      'repo_owner_username': 'louise',
                                      'times_downloaded': 164},
                       'score': 4.92},
                      {'matched_terms': [],
                       'repository': {'approved': 'no',
                                      'description': 'Convert BAM file to fastq',
                                      'full_last_updated': '2015-04-07 11:57 AM',
                                      'homepage_url': '',
                                      'id': '175812cd7caaf439',
                                      'last_updated': 'less than a month',
                                      'long_description': 'Use Picards SamToFastq to convert a BAM file to fastq. Useful for storing reads as BAM in Galaxy and converting to fastq when needed for analysis.',
                                      'name': 'bam_to_fastq',
                                      'remote_repository_url': '',
                                      'repo_owner_username': 'brad-chapman',
                                      'times_downloaded': 138},
                       'score': 4.14}],
             'hostname': 'https://testtoolshed.g2.bx.psu.edu/',
             'page': '1',
             'page_size': '2',
             'total_results': '64'}
    """
    return ctx.ti.repositories.search_repositories(q, page=page, page_size=page_size)
