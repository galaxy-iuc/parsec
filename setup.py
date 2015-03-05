#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Click',
    'bioblend',
    'wrapt',
]

test_requirements = [
    # TODO: put package test requirements here
]

version = '0.9.2'

setup(
    name='parsec',
    version=version,
    description='Command-line utilities to assist in interacting with Galaxy servers (http://galaxyproject.org/).',
    author='Galaxy Project and Community',
    author_email='rasche.eric@gmail.com',
    url='https://github.com/galaxy-iuc/parsec',
    packages=[
        'parsec',
        'parsec.commands',
    ],
    entry_points='''
        [console_scripts]
        parsec=parsec.cli:parsec
    ''',
    package_dir={'parsec': 'parsec'},
    install_requires=requirements,
    license="AFL",
    keywords='parsec',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
