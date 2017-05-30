.. _Quick_Start:

Quick Start
===========

This **Quick Start Tutorial** will walk you through every step of downloading,
installing, and running the fluidigm2purc pipeline. The details of each step can
be found in the main documentation.

**Basic requirements**:

- Python (we suggest using `Miniconda <https://conda.io/miniconda.html>`_)
- Python packages: pandas, numpy, biopython
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

``conda install cython``.

.. code:: bash

  git clone https://bitbucket.org/crothfels/purc.git
  cd purc && ./install_dependencies.sh

  # while in the PURC directory, add it to your PATH
  # It's best to add the PATH to your .bash_profile
  export PATH=$(pwd):$PATH

fluidigm2purc
^^^^^^^^^^^^^

.. code:: bash

  git clone https://github.com/pblischak/fluidigm2purc.git
  cd fluidigm
  make && sudo make install

2. Running the fluidigm2purc script
-----------------------------------

.. code:: bash

  fluidigm2purc -f FluidigmData

3. Running PURC
---------------

.. code:: bash

  purc_recluster.py

4. Processing PURC clusters
---------------------------

.. code:: bash

  crunch_clusters -i Loc1_clustered_reconsensus.afa -s output-taxon-table.txt \
                  -e output-locus-err.txt -l Loc1

5. Downstream
-------------
