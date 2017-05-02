import os

import click

from parsec.cli import pass_context
from parsec import config
from parsec.io import warn, info

CONFIG_TEMPLATE = """## Parsec Global Configuration File.
# Each stanza should contian a single galaxy server to control.
#
# You can set the key __default to the name of a default instance
# __default: local

local:
    key: "%(key)s"
    email: "<TODO>"
    password: "<TODO>"
    url: "%(url)s"
    admin: %(admin)s
"""

SUCCESS_MESSAGE = (
    "Wrote configuration template to %s, "
    "please open with editor and fill out."
)


@click.command("config_init")
@click.option(
    '--url',
    help="URL to galaxy server",
)
@click.option(
    '--api_key',
    help="API key for galaxy server",
)
@click.option(
    '--admin',
    is_flag=True,
    help="This API key is an admin/master API key",
)
@pass_context
def cli(ctx, url=None, api_key=None, admin=False, **kwds):
    """Help initialize global configuration (in home directory)
    """
    # TODO: prompt for values someday.
    config_path = config.global_config_path()
    if os.path.exists(config_path):
        warn("File %s already exists, exiting." % config_path)
        return -1
    with open(config_path, "w") as f:
        f.write(
            CONFIG_TEMPLATE % {
                'key': '<TODO>' if api_key is None else api_key,
                'url': '<TODO>' if url is None else url,
                'admin': admin})
        info(SUCCESS_MESSAGE % config_path)
