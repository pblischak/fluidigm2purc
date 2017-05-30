.. _Quick_Start:

Quick Start
===========

This **Quick Start Tutorial** will walk you through every step of downloading,
installing, and running the fluidigm2purc pipeline. The details of each step can
be found in the main documentation.

**Requirements**:

- Python (we suggest using `Miniconda <https://conda.io/miniconda.html>`_)
- Python modules: pandas, numpy, biopython
- C, C++ compilers (Linux should be good, Mac OSX needs Xcode and the **Command Line Tools**)
- PURC (available on Bitbucket)

1. Downloading and Installation
-------------------------------

Python
^^^^^^



.. code:: bash

  # Get Miniconda for your operating system (Mac or Linux)
  # Answer yes to the questions the Installer asks
  # These commands will download Python 2.7 for Mac OSX
  curl -O https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
  bash Miniconda2-latest-MacOSX-x86_64.sh

  # Install packages with conda or pip command
  conda install numpy pandas biopython
  # pip install numpy pandas biopython

PURC
^^^^

In addition to the Python modules that we already installed, PURC needs the Cython
module, which can be installed using the conda command: ``conda install cython``.

.. code:: bash

  git clone https://bitbucket.org/crothfels/purc.git
  cd purc && ./install_dependencies.sh

  # while in the PURC directory, add it to your PATH
  # It's best to add the PATH to your .bash_profile
  export PATH=$(pwd):$PATH

If you are on a Linux xomputer, you may have to run the ``install_dependencies_linux.sh``
script instead. The `Bitbucket repository for PURC <https://bitbucket.org/crothfels/purc/src/>`_
has more details about installation as well.

fluidigm2purc
^^^^^^^^^^^^^

.. code:: bash

  git clone https://github.com/pblischak/fluidigm2purc.git
  cd fluidigm
  make && sudo make install

2. Running fluidigm2purc
------------------------

The fluidigm2purc script will process a set of paired-end FASTQ files and will
output a single FASTA file for each locus present in the file with sequence header information
in the format required by PURC. As an example, let's say that we have our paired-end data
in the files ``FluidigmData_R1.fastq.gz`` and ``FluidigmData_R2.fastq.gz``. To run these
data through the script, all we would need to run is:

.. code:: bash

  fluidigm2purc -f FluidigmData

This will trim the data using the program Sickle, merge the paired-ends (if possible)
using FLASH2, and then write everything to a FASTA file in a new directory titles ``output-FASTA/``.
If we want to tweak some of the settings for the parameters that are used to filter/merge reads, we can
specify them using command line flags (type ``fluidigm2purc -h`` to see options).
In addition to the FASTA files, the fluidigm2purc script outputs two other files:
(1) a table containing all individuals where their ploidy level can be specified
(``output-taxon-table.txt``) and (2) a table with per locus error rates
(``output-locus-err.txt``).

3. Running PURC
---------------

.. code:: bash

  purc_recluster.py

4. Processing PURC clusters
---------------------------

.. code:: bash

  crunch_clusters -i loc1_clustered_reconsensus.afa -s output-taxon-table.txt \
                  -e output-locus-err.txt -l loc1

5. Downstream
-------------

Once all of the loci have been haplotyped, some of them may contain an excessive
amount of gaps from being aligned to bad clusters (or because reads neve merged).
A great tool for cleaning gappy alignments is `phyutility <http://blackrim.org/programs/phyutility/>`_.

**Example**:

.. code:: bash

  # Remove sites with more than 40% gaps
  phyutility -clean 0.4 loc1_crunched_clusters.fasta
