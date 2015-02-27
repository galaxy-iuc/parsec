import os

import click

from parsec.cli import pass_context
from parsec import options
from parsec import config
from parsec.io import warn, info

CONFIG_TEMPLATE = """## Parsec Global Configuration File.
# Each stanza should contian a single galaxy server to control.

local:
    key: "<TODO>"
    email: "<TODO>"
    password: "<TODO>"
test.galaxyproject:
    key: "<TODO>"
    email: "<TODO>"
    password: "<TODO>"
"""
SUCCESS_MESSAGE = (
    "Wrote configuration template to %s, "
    "please open with editor and fill out."
)


@click.command("config_init")
@options.optional_project_arg(exists=None)
@click.option(
    '--template',
    default=None
)
@pass_context
def cli(ctx, path, template=None, **kwds):
    """Help initialize global configuration (in home directory)
    """
    # TODO: prompt for values someday.
    config_path = config.global_config_path()
    if os.path.exists(config_path):
        warn("File %s already exists, exiting." % config_path)
        return -1
    with open(config_path, "w") as f:
        f.write(CONFIG_TEMPLATE)
        info(SUCCESS_MESSAGE % config_path)
