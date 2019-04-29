import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


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
@dict_output
def cli(ctx, q, page=1, page_size=10):
    """Search for repositories in a Galaxy Tool Shed.

Output:

    dictionary containing search hits as well as metadata for the
          search.
          For example::

            {u'hits': [{u'matched_terms': [],
               u'repository': {u'approved': u'no',
                u'description': u'Convert export file to fastq',
                u'full_last_updated': u'2015-01-18 09:48 AM',
                u'homepage_url': u'',
                u'id': u'bdfa208f0cf6504e',
                u'last_updated': u'less than a year',
                u'long_description': u'This is a simple too to convert Solexas Export files to FASTQ files.',
                u'name': u'export_to_fastq',
                u'remote_repository_url': u'',
                u'repo_owner_username': u'louise',
                u'times_downloaded': 164},
               u'score': 4.92},
              {u'matched_terms': [],
               u'repository': {u'approved': u'no',
                u'description': u'Convert BAM file to fastq',
                u'full_last_updated': u'2015-04-07 11:57 AM',
                u'homepage_url': u'',
                u'id': u'175812cd7caaf439',
                u'last_updated': u'less than a month',
                u'long_description': u'Use Picards SamToFastq to convert a BAM file to fastq. Useful for storing reads as BAM in Galaxy and converting to fastq when needed for analysis.',
                u'name': u'bam_to_fastq',
                u'remote_repository_url': u'',
                u'repo_owner_username': u'brad-chapman',
                u'times_downloaded': 138},
               u'score': 4.14}],
             u'hostname': u'https://testtoolshed.g2.bx.psu.edu/',
             u'page': u'1',
             u'page_size': u'2',
             u'total_results': u'64'}
    """
    return ctx.gi.repositories.search_repositories(q, page=page, page_size=page_size)
