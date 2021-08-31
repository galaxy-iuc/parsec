import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, text_output


@click.command('get_repository_revision_install_info')
@click.argument("name", type=str)
@click.argument("owner", type=str)
@click.argument("changeset_revision", type=str)
@pass_context
@custom_exception
@text_output
def cli(ctx, name, owner, changeset_revision):
    """Return a list of dictionaries of metadata about a certain changeset revision for a single tool.

Output:

    Returns a list of the following dictionaries:

          #. a dictionary defining the repository
          #. a dictionary defining the repository revision (RepositoryMetadata)
          #. a dictionary including the additional information required to
             install the repository

          For example::

            [{'deleted': False,
              'deprecated': False,
              'description': 'Galaxy Freebayes Bayesian genetic variant detector tool',
              'homepage_url': '',
              'id': '491b7a3fddf9366f',
              'long_description': 'Galaxy Freebayes Bayesian genetic variant detector tool originally included in the Galaxy code distribution but migrated to the tool shed.',
              'name': 'freebayes',
              'owner': 'devteam',
              'private': False,
              'remote_repository_url': '',
              'times_downloaded': 269,
              'type': 'unrestricted',
              'url': '/api/repositories/491b7a3fddf9366f',
              'user_id': '1de29d50c3c44272'},
             {'changeset_revision': 'd291dc763c4c',
              'do_not_test': False,
              'downloadable': True,
              'has_repository_dependencies': False,
              'id': '504be8aaa652c154',
              'includes_datatypes': False,
              'includes_tool_dependencies': True,
              'includes_tools': True,
              'includes_tools_for_display_in_tool_panel': True,
              'includes_workflows': False,
              'malicious': False,
              'repository_id': '491b7a3fddf9366f',
              'url': '/api/repository_revisions/504be8aaa652c154'},
             {'freebayes': ['Galaxy Freebayes Bayesian genetic variant detector tool',
                            'http://testtoolshed.g2.bx.psu.edu/repos/devteam/freebayes',
                            'd291dc763c4c',
                            '9',
                            'devteam',
                            {},
                            {'freebayes/0.9.6_9608597d12e127c847ae03aa03440ab63992fedf': {'changeset_revision': 'd291dc763c4c',
                                                                                          'name': 'freebayes',
                                                                                          'repository_name': 'freebayes',
                                                                                          'repository_owner': 'devteam',
                                                                                          'type': 'package',
                                                                                          'version': '0.9.6_9608597d12e127c847ae03aa03440ab63992fedf'},
                             'samtools/0.1.18': {'changeset_revision': 'd291dc763c4c',
                                                 'name': 'samtools',
                                                 'repository_name': 'freebayes',
                                                 'repository_owner': 'devteam',
                                                 'type': 'package',
                                                 'version': '0.1.18'}}]}]
    """
    return ctx.ti.repositories.get_repository_revision_install_info(name, owner, changeset_revision)
