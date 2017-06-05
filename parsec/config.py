from __future__ import absolute_import
import os
import yaml

DEFAULT_CONFIG = {
}

_config_path = os.environ.get(
    "PARSEC_GLOBAL_CONFIG_PATH",
    "~/.parsec.yml"
)
_config_path = os.path.expanduser(_config_path)
DEFAULT_CONFIG['config_path'] = _config_path


def global_config_path():
    return DEFAULT_CONFIG['config_path']


def set_global_config_path(config_path):
    DEFAULT_CONFIG['config_path'] = config_path


def read_global_config():
    config_path = global_config_path()
    if not os.path.exists(config_path):
        return DEFAULT_CONFIG

    with open(config_path) as f:
        return yaml.load(f)
