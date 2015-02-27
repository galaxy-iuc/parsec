import click

from parsec.cli import pass_context
from parsec.io import error, info
from parsec import options
from bioblend import galaxy


@click.command('add_user')
@options.galaxy_instance()

@click.option(
    '--username',
    help="Username for the new user",
)

@click.option(
    '--email',
    help="Email for the new user",
)

@click.option(
    '--password',
    help="Password for the new user",
)

@click.option(
    '--remote',
    is_flag=True,
    help="This galaxy instance is configured for REMOTE_USER",
)
@pass_context
def cli(ctx, galaxy_instance, username, email, password, remote=False, **kwds):
    """Add a user to a galaxy instance
    """
    global_config = ctx.global_config
    if galaxy_instance not in global_config:
        # TODO: refactor
        error("Unknown Galaxy instance, add to ~/.planemo.yml")
        return -1

    if 'admin' not in global_config[galaxy_instance] or not \
            global_config[galaxy_instance]['admin']:
        error("This must be an admin API key (set admin: True in ~/.planemo.yml)")
        return -2

    gi = galaxy.GalaxyInstance(':'.join([global_config[galaxy_instance]['host'],
                                         global_config[galaxy_instance]['port']]),
                               global_config[galaxy_instance]['key'])
    if remote:
        result = gi.users.create_remote_user(email)
    else:
        result = gi.users.create_local_user(username, email, password)

    info("Created user %(username)s with id %(id)s." % result)
