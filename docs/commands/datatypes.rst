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

       [u'snpmatrix',
        u'snptest',
        u'tabular',
        u'taxonomy',
        u'twobit',
        u'txt',
        u'vcf',
        u'wig',
        u'xgmml',
        u'xml']
   
    
**Options**::


      --extension_only TEXT
      --upload_only TEXT
      -h, --help             Show this message and exit.
    

``get_sniffers`` command
------------------------

**Usage**::

    parsec datatypes get_sniffers [OPTIONS]

**Help**

Get the list of all installed sniffers.


**Output**


A list of sniffer names.
     For example::

       [u'galaxy.datatypes.tabular:Vcf',
        u'galaxy.datatypes.binary:TwoBit',
        u'galaxy.datatypes.binary:Bam',
        u'galaxy.datatypes.binary:Sff',
        u'galaxy.datatypes.xml:Phyloxml',
        u'galaxy.datatypes.xml:GenericXml',
        u'galaxy.datatypes.sequence:Maf',
        u'galaxy.datatypes.sequence:Lav',
        u'galaxy.datatypes.sequence:csFasta']
   
    
**Options**::


      -h, --help  Show this message and exit.
    
