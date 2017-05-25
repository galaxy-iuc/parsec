========
Cookbook
========

This page will contain more easy "recipes" for using parsec as time goes
on. Short tips and tricks that can help you use it more effectively, or
short recipes that can document how to do more complex tasks.

Talking to multiple Galaxies
----------------------------

If you are regularly switching between multiple Galaxy instances, you'll
probably want to take advantage of the environment variable for
specifying a Galaxy instance. E.g.:

.. code-block:: shell

    $ PARSEC_GALAXY_INSTANCE=uni-admin parsec config get_config | jq .brand
    "Internal"
    $ PARSEC_GALAXY_INSTANCE=uni-public parsec config get_config | jq .brand
    "Public"

You could easily set these at the top of a parsec script you've built
and all commands from there on would talk to the same Galaxy instance.

Capturing execution state as XUnit Output
-----------------------------------------

If you find yourself building a pipeline with ``parsec`` and ``jq``, you might find
yourself wanting to produce the output in a machine-legible format such as
XUnit. ``parsec`` now ships with a (very alpha) script to help with this.
``parsec utils xunit_xargs`` provides an ``xargs``-like experience, except it
produces XUnit formatted output. We'll run through a quick example of this:

.. code-block:: shell

    parsec histories get_histories | \
    jq '.[].id' -r | \
    head -n 3 | \
    parsec utils xunit_xargs parsec histories get_status \| jq .percent_complete

This command will fetch the first three histories, and then attempt to run
``parsec histories get_status <history_id> | jq .percent_complete`` for each
history id passed in.

.. code-block:: xml

    <?xml version="1.0" ?>
    <testsuites errors="0" failures="0" tests="3" time="1.5296571254730225">
            <testsuite errors="0" failures="0" name="Parsec XX" skipped="0" tests="3" time="1.5296571254730225">
                    <testcase classname="parsec.histories.get_status.769f01a3981796db_|.jq..percent_complete" name="parsec.histories.get_status.769f01a3981796db_" time="0.518695">
                            <system-out>100</system-out>
                    </testcase>
                    <testcase classname="parsec.histories.get_status.83fbc32772cb5fcf_|.jq..percent_complete" name="parsec.histories.get_status.83fbc32772cb5fcf_" time="0.505619">
                            <system-out>100</system-out>
                    </testcase>
                    <testcase classname="parsec.histories.get_status.90c9282cb8718062_|.jq..percent_complete" name="parsec.histories.get_status.90c9282cb8718062_" time="0.505343">
                            <system-out>97.82608695652173</system-out>
                    </testcase>
            </testsuite>
    </testsuites>

Here we can see the example output, every test case listed, stdout has been captured.
