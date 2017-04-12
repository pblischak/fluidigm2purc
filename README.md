## `fluidigm2purc`

Conversion script for demultiplexed Fluidigm data for input to `PURC`.

### Installation

To obtain and install `fluidigm2purc` and its dependencies
([`Sickle`](https://github.com/najoshi/sickle),
[`PEAR`](https://github.com/xflouris/PEAR)),
run the following commands in a terminal:

```bash
git clone https://github.com/pblischak/fluidigm2purc.git fluidigm2purc
cd fluidigm2purc
make
sudo make install
make clean
```

`Sickle` is downloaded and installed but it not necessarily needed because
`PEAR` will perform read trimming as well. The option to trim reads with `Sickle`
prior to merging with `PEAR` is also available.

### Running `fluidigm2purc`

The list of options can be viewed by typing `fluidigm2purc -h`. The only manditory
option is the prefix for the paired-end FASTQ files (e.g., 'FluidigmData' for the files
FluidigmData_R1.fastq.gz and FluidigmData_R2.fastq.gz).

```bash
fluidigm2purc --prefix FluidigmData
```

Additional options can be specified to control parameters for file output,
multithreading, and trimming/merging reads.
