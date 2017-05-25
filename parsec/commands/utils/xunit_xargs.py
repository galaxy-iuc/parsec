import sys
import time
import click
import tempfile
import json
try:
    import StringIO as io
except:
    import io

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception
from justbackoff import Backoff
from subprocess import CalledProcessError, check_output
from xunit_wrapper import xunit, xunit_suite, xunit_dump
from six import binary_type, string_types, text_type


def unicodify(value):
    # From Galaxy
    if value is None:
        return None
    try:
        if not isinstance(value, string_types) and not isinstance(value, binary_type):
            value = str(value)
        if not isinstance(value, text_type):
            value = text_type(value, 'utf-8', 'replace')
    except Exception:
        return "error converting to unicode"
    return value


@click.command('xunit_xargs', context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True
))
@click.argument("_")

@pass_context
@bioblend_exception
def cli(ctx, _):
    """xargs look-alike that wraps output calls as XUnit XML

    e.g.::

        parsec histories get_histories | \
            jq '.[].id' -r | \
            head -n 3 | \
            parsec utils xunit_xargs parsec histories get_status \| jq .percent_complete

    will fetch the first three histories mentioned, and then pass them to xargs
    to run ``parsec histories get_status [history_id] | jq .percent_complete``. This will
    in turn produce XUnit XML that can be used in Jenkins or similar systems::

        <?xml version="1.0" ?>
        <testsuites errors="0" failures="0" tests="3" time="1.5944418907165527">
                <testsuite errors="0" failures="0" name="Parsec XX" skipped="0" tests="3" time="1.5944418907165527">
                        <testcase classname="parsec.histories.get_status.769f01a3981796db_|.jq..percent_complete" name="parsec.histories.get_status.769f01a3981796db_" time="0.604831">
                                <system-out>100</system-out>
                        </testcase>
                        <testcase classname="parsec.histories.get_status.83fbc32772cb5fcf_|.jq..percent_complete" name="parsec.histories.get_status.83fbc32772cb5fcf_" time="0.483556">
                                <system-out>100</system-out>
                        </testcase>
                        <testcase classname="parsec.histories.get_status.90c9282cb8718062_|.jq..percent_complete" name="parsec.histories.get_status.90c9282cb8718062_" time="0.506056">
                                <system-out>97.82608695652173</system-out>
                        </testcase>
                </testsuite>
        </testsuites>
    """
    test_cases = []
    for line in sys.stdin:
        # pretend to be xargs

        piped_commands = sys.argv[sys.argv.index('xunit_xargs') + 1:]
        if '|' in piped_commands:
            pipe_idx = piped_commands.index('|')
            piped_commands[pipe_idx] = line.strip() + ' |'
            built_command = piped_commands
        else:
            built_command = piped_commands + [line.strip()]
        # TODO: detect spaces in args and warn that they should be quoted.
        # If they provide multiple strings, then pipe them together

        xunit_identifier = '.'.join([x.strip().replace(' ', '_') for x in piped_commands])
        xunit_identifier.replace(' ', '_')
        if '|' in xunit_identifier:
            xunit_name = xunit_identifier[0:xunit_identifier.index('|')]
        else:
            xunit_name = xunit_identifier

        stderr = tempfile.NamedTemporaryFile()
        output = ""
        with xunit(xunit_name, xunit_identifier) as test_case:
            ctx.vlog('Executing: %s', ' '.join(built_command))
            output = check_output(' '.join(built_command), shell=True, stderr=stderr)

        # Set stdout
        stderr.seek(0)
        test_case._tc.stdout = unicodify(output).strip()
        test_case._tc.stderr = unicodify(stderr.read()).strip()
        # Append to list
        test_cases.append(test_case)

    ts = xunit_suite('Parsec XX', test_cases)
    print(xunit_dump([ts]))
