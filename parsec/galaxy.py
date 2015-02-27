from bioblend import galaxy
from .config import read_global_config

def get_galaxy_instance(instance_name):
    # I don't like reading the config twice.
    conf = read_global_config()
    if instance_name not in conf:
        raise Exception("Unkonwn Galaxy instance; check spelling or add to ~/.planemo.yml")

    return galaxy.GalaxyInstance(conf[instance_name]['url'],
                                 conf[instance_name]['key'])
