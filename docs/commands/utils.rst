utils
=====

This section is auto-generated from the help text for the arrow command
``utils``.


``wait_on_invocation`` command
------------------------------

**Usage**::

    parsec utils wait_on_invocation [OPTIONS] WORKFLOW_ID INVOCATION_ID

**Help**

Given a workflow and invocation id, wait until that invocation is
complete (or one or more steps have errored)

**Options**::


      --exit_early         Exit immediately after checking status rather than
                           sleeping indefinitely
      --backoff_min FLOAT  Minimum time to sleep between checks, in seconds.
      --backoff_max FLOAT  Maximum time to sleep between checks, in seconds
      -v, --verbose
      -h, --help           Show this message and exit.
    
