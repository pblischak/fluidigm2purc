.. _Getting_Started:

Getting Started
===============

Requirements
------------

-  Python
-  Python modules:

   -  numpy
   -  pandas
   -  biopython
   -  cython

-  C, C++ compilers (Mac users need Xcode Command Line Tools)
-  zlib (needed for Sickle)
-  `PURC <https://bitbucket.org/crothfels/purc>`_

Installation
------------

.. code:: bash

    git clone https://github.com/pblischak/fluidigm2puc.git
    cd fluidigm2purc
    make
    sudo make install

The Makefile will clone Sickle and FLASH2 from GitHub and will compile
them from source into a folder called ``deps/``. You'll need to have C and C++ compilers
to do this. Typing ``sudo make install`` will copy the fluidigm2purc scripts
and all of the dependencies to ``/usr/local/bin`` so that you can
run everything from anywhere on your computer.
