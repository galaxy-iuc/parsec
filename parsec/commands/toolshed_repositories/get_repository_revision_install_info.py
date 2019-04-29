import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_repository_revision_install_info')
@click.argument("name", type=str)
@click.argument("owner", type=str)
@click.argument("changeset_revision", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, name, owner, changeset_revision):
    """Return a list of dictionaries of metadata about a certain changeset revision for a single tool.

Output:

    Returns a list of the following dictionaries:

          #. a dictionary defining the repository
          #. a dictionary defining the repository revision (RepositoryMetadata)
          #. a dictionary including the additional information required to
             install the repository

          For example::

                     [{u'deleted': False,
                       u'deprecated': False,
                       u'description': u'Galaxy Freebayes Bayesian genetic variant detector tool',
                       u'homepage_url': u'',
                       u'id': u'491b7a3fddf9366f',
                       u'long_description': u'Galaxy Freebayes Bayesian genetic variant detector tool originally included in the Galaxy code distribution but migrated to the tool shed.',
                       u'name': u'freebayes',
                       u'owner': u'devteam',
                       u'private': False,
                       u'remote_repository_url': u'',
                       u'times_downloaded': 269,
                       u'type': u'unrestricted',
                       u'url': u'/api/repositories/491b7a3fddf9366f',
                       u'user_id': u'1de29d50c3c44272'},
                      {u'changeset_revision': u'd291dc763c4c',
                       u'do_not_test': False,
                       u'downloadable': True,
                       u'has_repository_dependencies': False,
                       u'id': u'504be8aaa652c154',
                       u'includes_datatypes': False,
                       u'includes_tool_dependencies': True,
                       u'includes_tools': True,
                       u'includes_tools_for_display_in_tool_panel': True,
                       u'includes_workflows': False,
                       u'malicious': False,
                       u'repository_id': u'491b7a3fddf9366f',
                       u'url': u'/api/repository_revisions/504be8aaa652c154'},
                      {u'freebayes': [u'Galaxy Freebayes Bayesian genetic variant detector tool',
                        u'http://testtoolshed.g2.bx.psu.edu/repos/devteam/freebayes',
                        u'd291dc763c4c',
                        u'9',
                        u'devteam',
                        {},
                        {u'freebayes/0.9.6_9608597d12e127c847ae03aa03440ab63992fedf': {u'changeset_revision': u'd291dc763c4c',
                          u'name': u'freebayes',
                          u'repository_name': u'freebayes',
                          u'repository_owner': u'devteam',
                          u'type': u'package',
                          u'version': u'0.9.6_9608597d12e127c847ae03aa03440ab63992fedf'},
                         u'samtools/0.1.18': {u'changeset_revision': u'd291dc763c4c',
                          u'name': u'samtools',
                          u'repository_name': u'freebayes',
                          u'repository_owner': u'devteam',
                          u'type': u'package',
                          u'version': u'0.1.18'}}]}]
    """
    return ctx.gi.repositories.get_repository_revision_install_info(name, owner, changeset_revision)
