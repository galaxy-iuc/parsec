jobs
====

This section is auto-generated from the help text for the parsec command
``jobs``.


``get_jobs`` command
--------------------

**Usage**::

    parsec jobs get_jobs [OPTIONS]

**Help**

Get the list of jobs of the current user.


**Output**


    list of dictionaries containing summary job information.
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
    
**Options**::


      -h, --help  Show this message and exit.
    

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

Report an error for a given job and dataset.


**Output**


    dict containing job error reply
    
**Options**::


      --email TEXT  Email to submit error report to
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
     This method can only be used with Galaxy ``release_20.09`` or later.
    
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
    

``search_jobs`` command
-----------------------

**Usage**::

    parsec jobs search_jobs [OPTIONS] JOB_INFO

**Help**

Return jobs for the current user based payload content.


**Output**


    list of dictionaries containing summary job information of
     the jobs that match the requested job run

   This method is designed to scan the list of previously run jobs and find
   records of jobs that had the exact some input parameters and datasets.
   This can be used to minimize the amount of repeated work, and simply
   recycle the old results.
    
**Options**::


      -h, --help  Show this message and exit.
    

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
    
