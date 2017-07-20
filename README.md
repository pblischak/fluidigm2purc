[![Build Status](https://travis-ci.org/pblischak/fluidigm2purc.svg?branch=master)](https://travis-ci.org/pblischak/fluidigm2purc) [![Documentation Status](https://readthedocs.org/projects/fluidigm2purc/badge/?version=latest)](http://fluidigm2purc.readthedocs.io/en/latest/?badge=latest) [![Docker Build Status](https://img.shields.io/docker/build/pblischak/fluidigm2purc.svg)](https://hub.docker.com/r/pblischak/fluidigm2purc/)

## **fluidigm2purc**: processing of paired-end Fluidigm data for analysis with PURC

## [**Read the Docs**](http://fluidigm2purc.readthedocs.io/en/latest/?badge=latest)

### Quick Introduction

To obtain and install fluidigm2purc and its dependencies
([Sickle](https://github.com/najoshi/sickle),
[FLASH2](https://github.com/dstreett/FLASH2)),
run the following commands in a terminal:

```bash
git clone https://github.com/pblischak/fluidigm2purc.git
cd fluidigm2purc
make
sudo make install
```

A standard run for fluidigm2purc will filter and trim reads with Sickle, merge
reads with FLASH2, and then process the resulting FASTQ files into FASTA files
with sequence headers compatible with PURC ("PURCifying").

### Running fluidigm2purc

This list of options can be viewed by typing `fluidigm2purc -h`. The only mandatory
option is the prefix for the paired-end FASTQ files (e.g., 'FluidigmData' for the files
FluidigmData_R1.fastq.gz and FluidigmData_R2.fastq.gz). Each step can be run individually
as well by specifying the name of the step with the `-p` flag.

```bash
# By default, the script will run all three steps (i.e., -p all)
fluidigm2purc -f FluidigmData

# To only run Sickle
fluidigm2purc -f FluidigmData -p sickle

# To only run FLASH2
fluidigm2purc -f FluidigmData -p flash2

# To only run the PURCifying step
fluidigm2purc -f FluidigmData -p PURCify
```

Additional options can be specified to control parameters for file output,
multithreading, and trimming/merging reads (see [Docs](http://fluidigm2purc.readthedocs.io/en/latest/?badge=latest)).
