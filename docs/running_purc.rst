.. _Running_PURC:

Running PURC
============

After running :ref:`fluidigm2purc <Fluidigm2Purc>`, you will have a new directory
named ``<OUTDIR>-FASTA`` (with whatever name you gave for ``OUTDIR``). The next
in the process is to run PURC. We will do this for each FASTA file individually
using a Bash for loop. The script from PURC that we will run is called
purc_recluster.py (make sure it is in your ``PATH``). The code below is an example
of what this would look like if you are running things on a Unix-flavored computer.

.. code:: bash

    cd OUTDIR-FASTA/

    # Loop through all of the fasta files and run purc_recluster.py
    for f in *.fasta
    do
        purc_recluster.py -f $f -o PURC_OUTDIR \
                          -c 0.95 0.975 0.99 0.995 -s 2 5 --clean
    done
