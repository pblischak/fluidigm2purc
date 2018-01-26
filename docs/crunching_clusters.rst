.. _Crunching_Clusters:

Processing PURC Clusters
========================

The *crunch_clusters* script takes the output from PURC and will determine
the haplotype configurations for your samples using the sizes of the resulting clusters.
These clusters are the output from :ref:`PURC <Running_PURC>`. To see all of the
options for running the script, type ``crunch_clusters -h``.

During this part of the pipeline, we use the taxon-ploidy table to determine the
number of haplotypes that should be output (e.g., a diploid should have 2, a tetraploid 4, etc.).
We also use the per locus error rates table to calculate the probability that a
given cluster is a sequencing error. The :ref:`Haplotyping Tutorial <Haplotyping>`
provides details on the mathematical model that we use for this step.

.. code:: bash

  crunch_clusters --input_fasta loc1_clustered_reconsensus.afa \
                  --species_table output-taxon-table.txt \
                  --error_rates output-locus-err.txt --locus_name loc1

We can also treat the locus as haploid by specifying the ``--haploid`` flag.
This can be used for chloroplast or mitochondrial loci, as well as for nuclear
loci when all we want is the primary cluster.

To go through all of the clustered loci, we can use a bash script and a for loop
to analyze each locus. If the loci under consideration are haploid, add the
``--haploid`` flag.

.. code:: bash

  # List all of the loci using the error rates file
  for l in $(tail +2 output-locus-err.txt | awk '{print $1}')
  do
    crunch_clusters -i ${l}_clustered_reconsensus.afa -s output-taxon-table.txt \
                    -e output-locus-err.txt -l $l
  done

Some other useful options during this step include realigning the sequences using Mafft
(just add ``--realign`` to your command).
We can remove gappy sites using Phyutility as well.
This can be done by adding the ``--clean <%>`` flag. Just substitute the percent of gaps allowed per
site that you want to use for cleaning. We also also have an option to only return unique haplotypes using
the ``--unique_haps`` flag.

.. note::

  We have run into some issues with species' names when using Phyutility. First,
  it doesn't like the semicolons that PURC uses to delimit the different parts of the
  sequence identifier (species names, cluster #, cluster size). We use ``sed`` to substitute
  underscores for the semicolons automatically. Other characters such as dashes have created
  issues as well because they get automatically substituted for underscores and no longer match the
  original names. If you are running into issues with not getting any output from the ``crunch_clusters``
  script, make sure you check the names of the species in all of the files it writes to make sure that
  things are being inadvertently changed.
