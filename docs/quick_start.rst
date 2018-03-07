.. _Quick_Start:

Quick Start
===========

This **Quick Start Tutorial** will walk you through every step of downloading,
installing, and running the Fluidigm2PURC pipeline. The details of each step can
be found in the main documentation.

**Requirements**:

- Python (we suggest using `Miniconda <https://conda.io/miniconda.html>`_)
- Python modules: pandas, numpy, biopython, cython
- C, C++ compilers (Linux should be good, Mac OSX needs Xcode and the **Command Line Tools**)
- PURC (available on `Bitbucket <https://bitbucket.org/crothfels/purc>`_)

.. note::

  We have tested our scripts on Python 2.7, 3.5, and 3.6. However, **PURC has only been
  tested with Python 2.7.** We have also worked with others researchers who had trouble
  getting things run with Python 3. Therefore, we recommend using Python 2.7.

1. Downloading and Installation
-------------------------------

Python
^^^^^^

The code below will walk you through downloading and installing a Python distribution
using Miniconda, as well as all of the Python packages that needed to use Fluidigm2PURC.

.. code:: bash

  # Get Miniconda for your operating system (Mac or Linux)
  # Answer yes to the questions the Installer asks
  # These commands will download Python 2.7 for Mac OSX
  curl -O https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
  bash Miniconda2-latest-MacOSX-x86_64.sh

  # Install packages with conda or pip command
  conda install numpy pandas biopython cython
  # pip install numpy pandas biopython cython

PURC
^^^^

PURC is available on Bitbucket and can be cloned and installed using the code below.

.. code:: bash

  git clone https://bitbucket.org/crothfels/purc.git
  cd purc && ./install_dependencies.sh

  # while in the PURC directory, add it to your PATH
  # It's best to add the PATH to your .bash_profile
  export PATH=$(pwd):$PATH

If you are on a Linux computer, you may have to run the ``install_dependencies_linux.sh``
script instead. The `Bitbucket repository for PURC <https://bitbucket.org/crothfels/purc/src/>`_
has more details about installation as well.

We have also included a modified version of the *purc_recluster.py* script as part of our
pipeline (*purc_recluster2.py*). The only difference is that it conducts fewer iterations
of the chierma detection and clustering steps. If you would like to use it, make sure that
move or copy it from the Fluidigm2PURC folder into the main PURC folder.

.. note::

  For the PURC scripts to work, they need to be present in the main PURC folder
  that was cloned from Bitbucket. These scripts also need to be made available
  in your bash ``PATH`` variable (see code above).

Fluidigm2PURC
^^^^^^^^^^^^^

Fluidigm2PURC is available on GitHub and can be cloned and installed using the code below.

.. code:: bash

  git clone https://github.com/pblischak/fluidigm2purc.git
  cd fluidigm
  make && sudo make install

The haplotyping script, *crunch_clusters*, can optionally call the programs Mafft and Phyutility.
If you would like to use these tools, make sure that you install them on them your machine
and add them to your PATH.

2. Running *fluidigm2purc*
--------------------------

The *fluidigm2purc* script will process a set of paired-end FASTQ files that
have been demultiplexed using the program `dbcAmplicons <https://github.com/msettles/dbcAmplicons>`_
and will output a single FASTA file for each locus present using sequence header information
in the format required by PURC. As an example, let's say that we have our paired-end data
in the files ``FluidigmData_R1.fastq.gz`` and ``FluidigmData_R2.fastq.gz``. To run these
data through the script, all we would need to run is:

.. code:: bash

  fluidigm2purc -f FluidigmData

This will filter/trim the reads using the program Sickle, merge the paired-ends (if possible)
using FLASH2, and then write everything to a FASTA file in a new directory named ``output-FASTA/``.
If we want to tweak some of the settings for the parameters that are used to filter/merge reads, we can
specify them using command line flags (type ``fluidigm2purc -h`` to see options).
In addition to the FASTA files, the fluidigm2purc script outputs two other files:
(1) a table containing all individuals where their ploidy level can be specified
(``output-taxon-table.txt``) and (2) a table with per locus error rates
(``output-locus-err.txt``).

3. Running PURC
---------------

If we ``cd`` into the ``output-FASTA`` directory, we can run PURC using its *purc_recluster.py* script
to do sequence clustering and PCR chimera detection. If you want to use the *purc_recluster2.py* script,
make sure you move or copy it into the main PURC folder. Also, because *purc_recluster2.py* only
does three iterations of chimera detection and clustering, it only requires that two clustering
thresholds be specified using the ``-c`` argument (rather than the usual four).

The code below will loop through all of the FASTA files in the ``output-FASTA`` directory and
will write all of the output to a new directory named ``output-PURC/``.

.. code:: bash

  cd output-FASTA

  for f in *.fasta
  do
    purc_recluster.py -f $f -o output-PURC \
                      -c 0.975 0.99 0.995 0.997 -s 2 5 --clean
  done

4. Processing PURC clusters
---------------------------

The script to infer haplotypes from the clusters returned by PURC is called *crunch_cluster*.
If you ``cd`` into the directory where we wrote all of the PURC output, you can loop through each
locus and analyze each one in turn. If you know the ploidy levels for your organism,
you can add them to the ``output-taxon-table.txt`` file.

The code below will use the locus names in the ``output-locus-err.txt`` file to loop through
all of the output files from PURC to infer haplotypes. It will also realign the sequences clustering
Mafft (``--realign``), clean the sequences using Phyutility (``--clean 0.4``),
and will only return unique haplotypes for each sample.

.. code:: bash

  cd output-PURC

  for l in $(tail +2 ../../output-locus-err.txt | awk '{print $1}')
  do
    crunch_clusters -i ${l}_clustered_reconsensus.afa -s ../../output-taxon-table.txt \
                    -e ../../output-locus-err.txt -l $l --realign --clean 0.4 --unique_haps
  done

5. Downstream
-------------

Once all of the loci have been haplotyped, some of them may still contain an excessive
amount of gaps from being aligned to bad clusters (or because reads never merged).
We can use `Phyutility <http://blackrim.org/programs/phyutility/>`_ to clean these up one more time.

**Example**:

.. code:: bash

  # Remove sites with more than 40% gaps
  phyutility -clean 0.4 loc1_crunched_clusters.fasta
