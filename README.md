[![Build Status](https://travis-ci.org/pblischak/fluidigm2purc.svg?branch=master)](https://travis-ci.org/pblischak/fluidigm2purc) [![Documentation Status](https://readthedocs.org/projects/fluidigm2purc/badge/?version=latest)](http://fluidigm2purc.readthedocs.io/en/latest/?badge=latest) [![Docker Build Status](https://img.shields.io/docker/build/pblischak/fluidigm2purc.svg)](https://hub.docker.com/r/pblischak/fluidigm2purc/)

## **Fluidigm2PURC**: automated processing and haplotype inference for double-barcoded PCR amplicons

**Fluidigm2PURC Preprint:**

Blischak, P. D., M. Latvis, D. F. Morales-Briones, J. C. Johnson, V. S. Di Stilio,
A. D. Wolfe, and D. C. Tank. 2018. Fluidigm2PURC: automated processing and
haplotype inference for double-barcoded PCR amplicons. bioRxiv doi:
[10.1101/242677](https://doi.org/10.1101/242677).

## [**Read the Docs**](http://fluidigm2purc.readthedocs.io/en/latest/?badge=latest)

### Quick Introduction

Fluidigm2PURC has two main scripts for processing paired-end amplicon sequencing data
from the Fluidigm Access Array: *fluidigm2purc* and *crunch_clusters*.

 - *fluidigm2purc*: filter and trim reads with Sickle, merge
 reads with FLASH2, and then process the resulting FASTQ files into FASTA files
 with sequence headers compatible with PURC ("PURCifying").

 - *crunch_clusters*: infer haplotypes from PURC clustering output for diploids, polyploids,
 unknown ploidy, or any mix of the three.

To obtain and install Fluidigm2PURC and its required dependencies
([Sickle](https://github.com/najoshi/sickle) [requires zlib],
[FLASH2](https://github.com/dstreett/FLASH2)),
run the following commands in a terminal:

```bash
git clone https://github.com/pblischak/fluidigm2purc.git
cd fluidigm2purc
make
sudo make install
```

The *crunch_clusters* script can also realign and clean sequence clusters using
[Mafft](http://mafft.cbrc.jp/alignment/software/) and
[Phyutility](https://github.com/blackrim/phyutility/releases/tag/v2.7.1), respectively.
To take advantage of this functionality, install them and make sure that they are in your PATH.
For Phyutility, we use the Bash script (named `phyutility`) setup that wraps a call to the Java phyutility.jar file.
