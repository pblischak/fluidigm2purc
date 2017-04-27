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
   -  matplotlib

-  C, C++ compilers
-  `PURC <https://bitbucket.org/crothfels/purc>`__

Installation
------------

.. code:: bash

    git clone https://github.com/pblischak/fluidigm+puc.git
    cd fluidigm+purc
    make
    sudo make install

The ``make`` command will clone Sickle and FLASH2 from GitHub and will attempt
to compile them. Running ``sudo make install`` will copy everything to
``/usr/local/bin`` so that the scripts and executables can be run from anywhere
on your machine.
