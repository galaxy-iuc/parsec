import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_users')
@click.option(
    "--deleted",
    help="Whether to include deleted users",
    is_flag=True
)
@click.option(
    "--f_email",
    help="filter for user emails. The filter will be active for non-admin users only if the Galaxy instance has the ``expose_user_email`` option set to ``true`` in the ``config/galaxy.yml`` configuration file. This parameter is silently ignored for non-admin users in Galaxy ``release_15.01`` and earlier.",
    type=str
)
@click.option(
    "--f_name",
    help="filter for user names. The filter will be active for non-admin users only if the Galaxy instance has the ``expose_user_name`` option set to ``true`` in the ``config/galaxy.yml`` configuration file. This parameter is silently ignored in Galaxy ``release_15.10`` and earlier.",
    type=str
)
@click.option(
    "--f_any",
    help="filter for user email or name. Each filter will be active for non-admin users only if the Galaxy instance has the corresponding ``expose_user_*`` option set to ``true`` in the ``config/galaxy.yml`` configuration file. This parameter is silently ignored in Galaxy ``release_15.10`` and earlier.",
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, deleted=False, f_email="", f_name="", f_any=""):
    """Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.

Output:

    a list of dicts with user details.
                 For example::

                   [{u'email': u'a_user@example.com',
                     u'id': u'dda47097d9189f15',
                     u'url': u'/api/users/dda47097d9189f15'}]
    """
    return ctx.gi.users.get_users(deleted=deleted, f_email=f_email, f_name=f_name, f_any=f_any)
