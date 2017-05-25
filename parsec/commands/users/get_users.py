import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_users')

@click.option(
    "--deleted",
    help=""
)
@click.option(
    "--f_email",
    help="filter for user emails. The filter will be active for non-admin users only if the Galaxy instance has the ``expose_user_email`` option set to ``True`` in the ``config/galaxy.ini`` configuration file. This parameter is silently ignored for non-admin users in Galaxy ``release_15.01`` and earlier.",
    type=str
)
@click.option(
    "--f_name",
    help="filter for user names. The filter will be active for non-admin users only if the Galaxy instance has the ``expose_user_name`` option set to ``True`` in the ``config/galaxy.ini`` configuration file. This parameter is silently ignored in Galaxy ``release_15.10`` and earlier.",
    type=str
)
@click.option(
    "--f_any",
    help="filter for user email or name. Each filter will be active for non-admin users only if the Galaxy instance has the corresponding ``expose_user_*`` option set to ``True`` in the ``config/galaxy.ini`` configuration file. This parameter is silently ignored in Galaxy ``release_15.10`` and earlier.",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, deleted=False, f_email="", f_name="", f_any=""):
    """Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.
    """
    return ctx.gi.users.get_users(deleted=deleted, f_email=f_email, f_name=f_name, f_any=f_any)
