.. _Fluidigm2Purc:

Running fluidigm2purc
=====================

The fluidigm2purc script combines the tasks of read filtering/trimming based on
quality scores, merging filtered paired-end reads, and conversion of the resulting
output to the proper format for running through PURC.

**Steps**:

    #. Read trimming with `Sickle <https://github.com/najoshi/sickle>`_
    #. Paired read mergind with `FLASH2 <https://github.com/dstreett/FLASH2>`_
    #. Conversion from FASTQ to PURC-compatible FASTA format (PURCifying)

Run ``fluidigm2purc -h`` to see options.

.. code::

    # A typical, default run of fluidigm2purc
    fluidigm2purc -f PREFIX -o OUTDIR -j 4

Each of the steps listed above can be run individually as well. That way, if you
want to rerun one of the step with different setting, you don't have to start from
scratch. A particular step can be specified using the ``-p`` flag and the name
of the step you want to run (``sickle``, ``flash2``, ``PURCify``). By default,
the script will run all three steps (``all``).

The final output is a directory named ``<OUTDIR>-FASTA`` that has a single FASTA
file for each locus that was present in FASTQ files used as input.
