datatypes
=========

This section is auto-generated from the help text for the parsec command
``datatypes``.


``get_datatypes`` command
-------------------------

**Usage**::

    parsec datatypes get_datatypes [OPTIONS]

**Help**

Get the list of all installed datatypes.


**Output**


    A list of datatype names.
     For example::

       ['snpmatrix',
        'snptest',
        'tabular',
        'taxonomy',
        'twobit',
        'txt',
        'vcf',
        'wig',
        'xgmml',
        'xml']
    
**Options**::


      --extension_only  Return only the extension rather than the datatype name
      --upload_only     Whether to return only datatypes which can be uploaded
      -h, --help        Show this message and exit.
    

``get_sniffers`` command
------------------------

**Usage**::

    parsec datatypes get_sniffers [OPTIONS]

**Help**

Get the list of all installed sniffers.


**Output**


    A list of sniffer names.
     For example::

       ['galaxy.datatypes.tabular:Vcf',
        'galaxy.datatypes.binary:TwoBit',
        'galaxy.datatypes.binary:Bam',
        'galaxy.datatypes.binary:Sff',
        'galaxy.datatypes.xml:Phyloxml',
        'galaxy.datatypes.xml:GenericXml',
        'galaxy.datatypes.sequence:Maf',
        'galaxy.datatypes.sequence:Lav',
        'galaxy.datatypes.sequence:csFasta']
    
**Options**::


      -h, --help  Show this message and exit.
    
