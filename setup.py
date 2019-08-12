#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()

requirements = [
    'Click>=6.7',
    'bioblend==0.13.0',
    'wrapt',
    'pyyaml',
    'justbackoff',
    'xunit-wrapper>=0.12',
    'future',
]

test_requirements = [
    # TODO: put package test requirements here
]

# Update it in parsec/__init__.py
version = None
with open('parsec/__init__.py', 'r') as handle:
    versline = [x for x in handle.readlines() if 'version' in x][0].strip()
    _, vers = versline.split(' = ')
    version = vers.strip("'")


subpackages = [x.replace('/', '.') for x in glob.glob('parsec/commands/*') if not x.endswith('.py')]

setup(
    name='galaxy-parsec',
    version=version,
    description='Command-line utilities to assist in interacting with Galaxy servers (http://galaxyproject.org/).',
    long_description=readme,
    author='Galaxy Project and Community',
    author_email='parsec@hx42.org',
    url='https://github.com/galaxy-iuc/parsec',
    packages=[
        'parsec',
        'parsec.commands',
    ] + subpackages,
    entry_points='''
        [console_scripts]
        parsec=parsec.cli:parsec
    ''',
    package_dir={'parsec': 'parsec'},
    install_requires=requirements,
    license="AFL",
    keywords='parsec',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
