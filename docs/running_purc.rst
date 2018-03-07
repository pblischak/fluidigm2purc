.. _Running_PURC:

Running PURC
============

After running the *fluidigm2purc* script, you will have a new directory
named ``output-FASTA``. The next
in the process is to run PURC. We will do this for each FASTA file individually
using a Bash for loop. The script from PURC that we will run is called
*purc_recluster.py*. Make sure that it is in the main PURC folder and also that
it is in your ``PATH``. The code below is an example
of what this would look like if you are running things on a Unix-flavored computer.

.. code:: bash

    cd output-FASTA/

    # Loop through all of the fasta files and run purc_recluster.py
    for f in *.fasta
    do
        purc_recluster.py -f $f -o output-PURC \
                          -c 0.975 0.99 0.995 0.997 -s 2 5 --clean
    done

We have also included a modified version of the *purc_recluster.py* script as part of our
pipeline (*purc_recluster2.py*). The only difference is that it conducts fewer iterations
of the chimema detection and clustering steps. If you would like to use it, make sure that
move or copy it from the Fluidigm2PURC folder into the main PURC folder. Also, it
also only requires two clustering thresholds for the ``-c`` option.
