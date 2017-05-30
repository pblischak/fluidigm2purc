.. _Fluidigm2Purc:

Running fluidigm2purc
=====================

The fluidigm2purc script combines the tasks of read filtering/trimming based on
quality scores, merging filtered paired-end reads, and conversion of the resulting
output to the proper format for running through PURC. Run ``fluidigm2purc -h`` to
see options.

**Steps**:

    #. Read trimming with `Sickle <https://github.com/najoshi/sickle>`_
    #. Paired read mergind with `FLASH2 <https://github.com/dstreett/FLASH2>`_
    #. Conversion from FASTQ to PURC-compatible FASTA format ("PURCifying")

Each of the steps listed above can be run individually as well. That way, if you
want to rerun one of the step with different setting, you don't have to start from
scratch. A particular step can be specified using the ``-p`` flag and the name
of the step you want to run (``sickle``, ``flash2``, ``PURCify``). By default,
the script will run all three steps (``all``). The only mandatory
option is the prefix for the paired-end FASTQ files (e.g., 'FluidigmData' for the files
FluidigmData_R1.fastq.gz and FluidigmData_R2.fastq.gz), which is given using the
``-f`` flag.

.. code:: bash

    # By default, the script will run all three steps (i.e., --program all)
    fluidigm2purc -f FluidigmData

    # To only run Sickle
    fluidigm2purc -f FluidigmData -p sickle

    # To only run FLASH2
    fluidigm2purc -f FluidigmData -p flash2

    # To only run the PURCifying step
    fluidigm2purc -f FluidigmData -p PURCify

The final output is a directory named ``output-FASTA`` that has a single FASTA
file for each locus that was present in FASTQ files used as input. The ``output``
part of the directory cab be substituted with whatever is supplied by the ``-o``
argument (default=output).

PURCifying
----------

The conversion from FASTQ to FASTA is straightforward because FASTA only uses the
first two lines of every four line sequence entry in the FASTQ file. The important
bit here is that we grab the relevant information from the sequence header in
the FASTQ file and print it so that it is compatible with PURC. The things that
we want are the taxon name and the locus name. These are added by
`dbcAmplicons <https://github.com/msettles/dbcAmplicons>`_ when the Fluidigm
data are demultiplexed. **Taxon names and locus names can't
have spaces in them.** The code splits on spaces first, then on colons (":") so that it can
grab the taxon and locus names (this is specific to the way the Fluidigm data are processed
by dbcAmplicons). Merged reads from FLASH2 are processed first.
Unmerged reads are then read in together and are
artificially combined with eight N's in between ("NNNNNNNN").

Additional outputs
------------------

``output.log``
^^^^^^^^^^^^^^

The fluidigm2purc script will output a log file that lists the taxa and loci found
during the processing of the FASTQ files. It also lists the command line arguments
that were used to generate the analysis.

``output-taxon-table.txt``
^^^^^^^^^^^^^^^^^^^^^^^^^^

A two-column table listing each taxon and its ploidy level is generated so that
users can specify what the ploidy level of the sample is when processing the
clusters output by PURC (see the section on :ref:`cluster crunching <Crunching_Clusters>`).
By default, all of the ploidy values are set to ``None``.

**Example**:

.. code::

  Taxon    Ploidy
  taxon1   None
  taxon2   None
  .
  .
  .
  taxonN   None

``output-locus-err.txt``
^^^^^^^^^^^^^^^^^^^^^^^^

fluidigm2purc will also calculate the per locus error rate using the PHRED
quality scores in the FASTQ files. It does this by calculating the average error
for each read mapping to a locus, followed by the overall average across reads.
These error values are used in the :ref:`cluster crunching step <Crunching_Clusters>`
to determine if a cluster output by PURC is sequencing error or not.

**Example**:

.. code::

  Locus    Error
  loc1     0.002341729
  loc2     0.032134829
  .
  .
  .
  locN     0.000967257
