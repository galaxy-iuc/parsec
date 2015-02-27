""" Click definitions for various shared options and arguments.
"""
import click


def galaxy_instance():
    return click.option(
        "--galaxy_instance",
        help='name of galaxy instance per ~/.planemo.yml'
    )
