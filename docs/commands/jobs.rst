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
    

``search_jobs`` command
-----------------------

**Usage**::

    parsec jobs search_jobs [OPTIONS] JOB_INFO

**Help**

Return jobs for the current user based payload content.


**Output**


    
    
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

       {u'create_time': u'2014-03-01T16:17:29.828624',
        u'exit_code': 0,
        u'id': u'a799d38679e985db',
        u'inputs': {u'input': {u'id': u'ebfb8f50c6abde6d',
          u'src': u'hda'}},
        u'model_class': u'Job',
        u'outputs': {u'output': {u'id': u'a799d38679e985db',
          u'src': u'hda'}},
        u'params': {u'chromInfo': u'"/opt/galaxy-central/tool-data/shared/ucsc/chrom/?.len"',
          u'dbkey': u'"?"',
          u'seq_col': u'"2"',
          u'title_col': u'["1"]'},
        u'state': u'ok',
        u'tool_id': u'tab2fasta',
        u'update_time': u'2014-03-01T16:17:31.930728'}
   
    
**Options**::


      --full_details  when ``True``, the complete list of details for the given job.
      -h, --help      Show this message and exit.
    
