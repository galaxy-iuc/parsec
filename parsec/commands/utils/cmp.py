import sys
import time
import click
import json
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception
from justbackoff import Backoff
from subprocess import CalledProcessError, check_output
from xunit_wrapper import xunit, xunit_suite, xunit_dump
from six import binary_type, string_types, text_type


@click.command('cmp')
@click.argument("method", type=str, required=True)
@click.argument("cmp_with", type=str, required=True)

@pass_context
@bioblend_exception
def cli(ctx, method, cmp_with):
    """comparison tool. Exits if the value read from stdin does not pass the comparison test with the specified value.

    method is the comparison method. One of these (lt, gt, eq, ne) which will
    trigger a numerical comparison (cast to floats), or one of teq, tneq which
    will trigger a string comparison.

    cmp_with is the value to compare against. E.g. '100' or 'test'

    e.g.::

        echo '5' | parsec utils cmp lt 10 # exit 0

        echo '5' | parsec utils cmp lt 1 # exit 1

    """
    data = sys.stdin.read()
    if method in ('lt', 'gt', 'ne', 'eq'):
        data = float(data.strip())
        cmp_with = float(cmp_with.strip())

        if method == 'lt':
            ctx.exit(0) if data < cmp_with else sys.stderr.write('%s >= %s' % (data, cmp_with)); ctx.exit(1)
        elif method == 'gt':
            ctx.exit(0) if data > cmp_with else sys.stderr.write('%s <= %s' % (data, cmp_with)); ctx.exit(1)
        elif method == 'ne':
            ctx.exit(0) if data != cmp_with else sys.stderr.write('%s == %s' % (data, cmp_with)); ctx.exit(1)
        elif method == 'eq':
            ctx.exit(0) if data == cmp_with else sys.stderr.write('%s != %s' % (data, cmp_with)); ctx.exit(1)

    elif method in ('teq', 'tneq'):
        if method == 'tneq':
            ctx.exit(0) if data != cmp_with else sys.stderr.write('%s == %s' % (data, cmp_with)); ctx.exit(1)
        elif method == 'teq':
            ctx.exit(0) if data == cmp_with else sys.stderr.write('%s != %s' % (data, cmp_with)); ctx.exit(1)
    ctx.exit(2)
