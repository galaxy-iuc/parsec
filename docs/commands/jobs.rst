jobs
====

This section is auto-generated from the help text for the parsec command
``jobs``.


``cancel_job`` command
----------------------

**Usage**::

    parsec jobs cancel_job [OPTIONS] JOB_ID

**Help**

Cancel a job, deleting output datasets.


**Output**


    ``True`` if the job was successfully cancelled, ``False`` if
     it was already in a terminal state before the cancellation.
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_common_problems`` command
-------------------------------

**Usage**::

    parsec jobs get_common_problems [OPTIONS] JOB_ID

**Help**

Query inputs and jobs for common potential problems that might have resulted in job failure.


**Output**


    dict containing potential problems

   .. note::
     This method is only supported by Galaxy 19.05 or later.
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_destination_params`` command
----------------------------------

**Usage**::

    parsec jobs get_destination_params [OPTIONS] JOB_ID

**Help**

Get destination parameters for a job, describing the environment and location where the job is run.


**Output**


    Destination parameters for the given job

   .. note::
     This method is only supported by Galaxy 20.05 or later and requires
     the user to be an admin.
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_inputs`` command
----------------------

**Usage**::

    parsec jobs get_inputs [OPTIONS] JOB_ID

**Help**

Get dataset inputs used by a job.


**Output**


    Inputs for the given job
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_jobs`` command
--------------------

**Usage**::

    parsec jobs get_jobs [OPTIONS]

**Help**

Get all jobs, or select a subset by specifying optional arguments for filtering (e.g. a state).


**Output**


    Summary information for each selected job.
     For example::

       [{'create_time': '2014-03-01T16:16:48.640550',
         'exit_code': 0,
         'id': 'ebfb8f50c6abde6d',
         'model_class': 'Job',
         'state': 'ok',
         'tool_id': 'fasta2tab',
         'update_time': '2014-03-01T16:16:50.657399'},
        {'create_time': '2014-03-01T16:05:34.851246',
         'exit_code': 0,
         'id': '1cd8e2f6b131e891',
         'model_class': 'Job',
         'state': 'ok',
         'tool_id': 'upload1',
         'update_time': '2014-03-01T16:05:39.558458'}]

   .. note::
     The following filtering options can only be used with Galaxy ``release_21.05`` or later:
       user_id, limit, offset, workflow_id, invocation_id
    
**Options**::


      --state TEXT           Job states to filter on.
      --history_id TEXT      Encoded history ID to filter on.
      --invocation_id TEXT   Encoded workflow invocation ID to filter on.
      --tool_id TEXT         Tool IDs to filter on.
      --workflow_id TEXT     Encoded workflow ID to filter on.
      --user_id TEXT         Encoded user ID to filter on. Only admin users can
                             access the jobs of other users.
    
      --date_range_min TEXT  Mininum job update date (in YYYY-MM-DD format) to
                             filter on.
    
      --date_range_max TEXT  Maximum job update date (in YYYY-MM-DD format) to
                             filter on.
    
      --limit INTEGER        Maximum number of jobs to return.  [default: 500]
      --offset INTEGER       Return jobs starting from this specified position. For
                             example, if ``limit`` is set to 100 and ``offset`` to
                             200, jobs 200-299 will be returned.
    
      --user_details         If ``True`` and the user is an admin, add the user
                             email to each returned job dictionary.
    
      -h, --help             Show this message and exit.
    

``get_metrics`` command
-----------------------

**Usage**::

    parsec jobs get_metrics [OPTIONS] JOB_ID

**Help**

Return job metrics for a given job.


**Output**


    list containing job metrics

   .. note::
     Calling ``show_job()`` with ``full_details=True`` also returns the
     metrics for a job if the user is an admin. This method allows to fetch
     metrics even as a normal user as long as the Galaxy instance has the
     ``expose_potentially_sensitive_job_metrics`` option set to ``true`` in
     the ``config/galaxy.yml`` configuration file.
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_outputs`` command
-----------------------

**Usage**::

    parsec jobs get_outputs [OPTIONS] JOB_ID

**Help**

Get dataset outputs produced by a job.


**Output**


    Outputs of the given job
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_state`` command
---------------------

**Usage**::

    parsec jobs get_state [OPTIONS] JOB_ID

**Help**

Display the current state for a given job of the current user.


**Output**


    state of the given job among the following values: `new`,
     `queued`, `running`, `waiting`, `ok`. If the state cannot be
     retrieved, an empty string is returned.

   .. versionadded:: 0.5.3
    
**Options**::


      -h, --help  Show this message and exit.
    

``report_error`` command
------------------------

**Usage**::

    parsec jobs report_error [OPTIONS] JOB_ID DATASET_ID MESSAGE

**Help**

Report an error for a given job and dataset to the server administrators.


**Output**


    dict containing job error reply

   .. note::
     This method is only supported by Galaxy 20.01 or later.
    
**Options**::


      --email TEXT  Email for error report submission. If not specified, the email
                    associated with the Galaxy user account is used by default.
    
      -h, --help    Show this message and exit.
    

``rerun_job`` command
---------------------

**Usage**::

    parsec jobs rerun_job [OPTIONS] JOB_ID

**Help**

Rerun a job.


**Output**


    Information about outputs and the rerun job

   .. note::
     This method can only be used with Galaxy ``release_21.01`` or later.
    
**Options**::


      --remap                    when ``True``, the job output(s) will be remapped
                                 onto the dataset(s) created by the original job; if
                                 other jobs were waiting for this job to finish
                                 successfully, they will be resumed using the new
                                 outputs of this tool run. When ``False``, new job
                                 output(s) will be created. Note that if Galaxy does
                                 not permit remapping for the job in question,
                                 specifying ``True`` will result in an error.
    
      --tool_inputs_update TEXT  dictionary specifying any changes which should be
                                 made to tool parameters for the rerun job.
    
      --history_id TEXT          ID of the history in which the job should be
                                 executed; if not specified, the same history will
                                 be used as the original job run.
    
      -h, --help                 Show this message and exit.
    

``resume_job`` command
----------------------

**Usage**::

    parsec jobs resume_job [OPTIONS] JOB_ID

**Help**

Resume a job if it is paused.


**Output**


    dict containing output dataset associations

   .. note::
     This method is only supported by Galaxy 18.09 or later.
    
**Options**::


      -h, --help  Show this message and exit.
    

``search_jobs`` command
-----------------------

**Usage**::

    parsec jobs search_jobs [OPTIONS] TOOL_ID INPUTS

**Help**

Return jobs matching input parameters.


**Output**


    Summary information for each matching job

   This method is designed to scan the list of previously run jobs and find
   records of jobs with identical input parameters and datasets. This can
   be used to minimize the amount of repeated work by simply recycling the
   old results.

   .. versionchanged:: 0.16.0
     Replaced the ``job_info`` parameter with separate ``tool_id``,
     ``inputs`` and ``state``.

   .. note::
     This method is only supported by Galaxy 18.01 or later.
    
**Options**::


      --state TEXT  only return jobs in this state
      -h, --help    Show this message and exit.
    

``show_job`` command
--------------------

**Usage**::

    parsec jobs show_job [OPTIONS] JOB_ID

**Help**

Get details of a given job of the current user.


**Output**


    A description of the given job.
     For example::

       {'create_time': '2014-03-01T16:17:29.828624',
        'exit_code': 0,
        'id': 'a799d38679e985db',
        'inputs': {'input': {'id': 'ebfb8f50c6abde6d', 'src': 'hda'}},
        'model_class': 'Job',
        'outputs': {'output': {'id': 'a799d38679e985db', 'src': 'hda'}},
        'params': {'chromInfo': '"/opt/galaxy-central/tool-data/shared/ucsc/chrom/?.len"',
                   'dbkey': '"?"',
                   'seq_col': '"2"',
                   'title_col': '["1"]'},
        'state': 'ok',
        'tool_id': 'tab2fasta',
        'update_time': '2014-03-01T16:17:31.930728'}
    
**Options**::


      --full_details  when ``True``, the complete list of details for the given job.
      -h, --help      Show this message and exit.
    

``show_job_lock`` command
-------------------------

**Usage**::

    parsec jobs show_job_lock [OPTIONS]

**Help**

Show whether the job lock is active or not. If it is active, no jobs will dispatch on the Galaxy server.


**Output**


    Status of the job lock

   .. note::
     This method is only supported by Galaxy 20.05 or later and requires
     the user to be an admin.
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_job_lock`` command
---------------------------

**Usage**::

    parsec jobs update_job_lock [OPTIONS]

**Help**

Update the job lock status by setting ``active`` to either ``True`` or ``False``. If ``True``, all job dispatching will be blocked.


**Output**


    
    
**Options**::


      --active    The state of the job lock, locked=True
      -h, --help  Show this message and exit.
    

``wait_for_job`` command
------------------------

**Usage**::

    parsec jobs wait_for_job [OPTIONS] JOB_ID

**Help**

Wait until a job is in a terminal state.


**Output**


    Details of the given job.
    
**Options**::


      --maxwait FLOAT   Total time (in seconds) to wait for the job state to become
                        terminal. If the job state is not terminal within this time,
                        a ``TimeoutException`` will be raised.  [default: 12000]
    
      --interval FLOAT  Time (in seconds) to wait between 2 consecutive checks.
                        [default: 3]
    
      --check           Whether to check if the job terminal state is 'ok'.
                        [default: True]
    
      -h, --help        Show this message and exit.
    
