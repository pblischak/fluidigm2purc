.. Crunching_Clusters:

Processing PURC Clusters
========================

The crunch_clusters script takes the output from PURC and will determine
the haplotype configurations for your samples. These clusters are the output
from :ref:`PURC <Running_PURC>`. To see all of the options for running the script,
type `crunch_clusters -h`.

.. code:: bash

  crunch_clusters --input_fasta loc1_clustered_reconsensus.afa --species_table taxon_df.txt \
                  --error_rates error_df.txt --locus_name loc1

We can also treat the locus as haploid by specifying the`--haploid` flag.
This can be used for chloroplast or mirochondrial loci, as well as for nuclear
loci when all we want is the primary cluster.

To loop through all of the clustered loci, we can use a bash script and a for loop
to analyze each locus. If the loci under consideration are haploid, add the `-hap`
flag.

.. code:: bash

  # List all of the loci using the error rates file
  for l in $(tail +2 error_df.txt | awk '{print $1}')
  do
    crunch_clusters -i $l_clustered_reconsensus.afa -s taxon_df.txt \
                    -e error_df.txt -l $l
  done
