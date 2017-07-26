.. _Haplotyping:

Determining Haplotypes
======================

Unknown ploidy-level
--------------------

Inferring haplotype configurations for individuals with unknown ploidy levels
involves identifying which clusters are likely to be “real” haplotypes,
and which ones are likely to be errors.
We do this by considering a set of models that range from treating all clusters as errors,
to one where all clusters are real haplotypes.
The models in between successively treat the next cluster in the ordered set as a real haplotype (sorted by size).
For an individual with :math:`N` clusters, there are :math:`N+1` models to test.
Each of these models has :math:`H` real haplotypes :math:`(0,\ldots,H)` and :math:`N-H` errors
:math:`(H+1,...,N)`.
The likelihood for each of these models is the sum of the clusters sizes
:math:`(C1,...,CN)` times the log probility that they are sequencing errors :math:`(\epsilon)`
or not :math:`(1-\epsilon)`. The likelihood for a model with H real haplotypes is given by:

.. math::

    \ell_H = \sum_{i=0}^H C_i \times \log (1 - \epsilon) + \sum_{j>H}^N C_j \times \log (\epsilon).

To determine the most likely haplotype configuration,
we calculate how much the likelihood increases over the previous model
when another haplotype is added (the likelihood is monotonically increasing).
We also normalize these differences by the total change in likelihood from the model
with :math:`H=0` to the model with :math:`H=N`.
If this value is less than a given cutoff (we use a default of 0.10),
the previous model is treated as the best configuration.
Since the cluster sized are ordered, the increase in the log-likelihood will always be
smaller for any additional haplotypes.

Known ploidy-level
------------------

To infer the maximum likelihood haplotype configuration using integer partitions,
we use a multinomial likelihood that uses the size of each cluster being considered as a haplotype.
For an individual with ploidy level :math:`K`, we take the first :math:`K` clusters sorted by size and
calculate the likelihood for a given partition as follows:
each entry in a partition, :math:`P`, contains the number of times that a particular
haplotype is represented in the configuration.
Given cluster sizes :math:`C_1` through :math:`C_K` and a sequencing error rate of :math:`\epsilon`,
the log likelihood for a partition :math:`P` is:

.. math::

    \ell_P = \sum_{i=0}^{|P|} C_i \times \log\left(\frac{P[i]}{K}\right) + \sum_{j>|P|}^K C_j \times \log(\epsilon).

Here :math:`|P|` represents the size of the partition.
