## `fluidigm2purc`

Conversion script for demultiplexed Fluidigm data for input to `PURC`.

### Installation

To obtain and install `fluidigm2purc` and its dependencies
([`Sickle`](https://github.com/najoshi/sickle),
[`FLASH2`](https://github.com/dstreett/FLASH2),
[`PEAR`](https://github.com/xflouris/PEAR) [experimental]),
run the following commands in a terminal:

```bash
git clone https://github.com/pblischak/fluidigm2purc.git fluidigm2purc
cd fluidigm2purc
make
sudo make install
```

The Makefile will clone all of the dependencies from GitHub and will compile
them from source into a folder called `deps`. Typing `sudo make install` will copy
`fluidigm2purc` and all of the dependencies to `/usr/local/bin` so that you can
run everything from anywhere on your computer. Typing make clean will remove the
`deps/` folder since we don't need it after everything has been installed.

A standard run for `fluidigm2purc` will filter and trim reads with `Sickle`, merge
reads with `FLASH2`, and then process the resulting FASTQ files into FASTA files
with sequence headers compatible with `PURC` ("PURCifying").

The inclusion of `PEAR` is somewhat experimental because we haven't used it in the
past. It ostensibly does trimming and merging of reads. However, when one paired
read is removed, the other one may not be thrown out too (like with sickle), so
the non-combined reads may not match up. We have to test this out more.

### Running `fluidigm2purc`

```
usage: fluidigm2purc [-h] [-v] -f [-p] [-o] [-j] [-q] [-l]

Options for fluidigm2purc

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

required arguments:
  -f, --fastq_prefix    prefix for paired-end FASTQ files

additional arguments:
  -p, --program     program(s) to run [all]
  -o, --outname     base name for output fasta file [output]
  -j, --nthreads    number of threads to use for executables [1]
  -q, --quality     PHRED quality score cutoff [20]
  -l, --length      minimum length for Sickle trimming [100]
```

This list of options can be viewed by typing `fluidigm2purc -h`. The only manditory
option is the prefix for the paired-end FASTQ files (e.g., 'FluidigmData' for the files
FluidigmData_R1.fastq.gz and FluidigmData_R2.fastq.gz). Each step can be run individually
as well by specifying the name of the step with the `--program` flag.

```bash
# By default, the script will run all three steps (i.e., --program all)
fluidigm2purc --fastq_prefix FluidigmData

# To only run Sickle
fluidigm2purc --fastq_prefix FluidigmData --program sickle_cmd

# To only run FLASH2
fluidigm2purc --fastq_prefix FluidigmData --program flash2

# To only run the PURCifying step
fluidigm2purc --fastq_prefix FluidigmData --program PURCify
```

Additional options can be specified to control parameters for file output,
multithreading, and trimming/merging reads.
