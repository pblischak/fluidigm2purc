## `fluidigm2purc`

Conversion script for demultiplexed fluidigm data for input to `PURC`.

To install the dependencies, type `make`. Each of the necessary programs will be
cloned from GitHub and compiled in a folder called `deps/`.

```bash
fluidigm2purc --help

## Usage: fluidigm2purc.py {-h|-v} [options]
##
## Options:
##    --prefix <string>     Name for read 1 and read 2.
##    --taxa <string>       File with taxon names.
##    --loci <string>       File with locus names.
##    --outname <string>    Name of output FASTA file.
```
