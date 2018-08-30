#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pacbio_err.py
# Written by PD Blischak

"""
<< pacbio_err.py >>

Calculate global average level of sequencing error across all reads in
a FASTQ file from PacBio data. The FASTQ file can gzipped, but it doesn't
have to be.

Arguments
---------

  - infile <string> : name of input FASTQ file (can be gzipped or not)

Output
------

  For each read in the input FASTQ file, pacbio_err.py will first calculate
  the mean level of sequencing error per read. It then prints the grand mean
  (mean of means) to standard out. This is the value that should be used for
  each locus in the locus_err.txt table for the crunch_clusters script.
"""

from __future__ import print_function, division
from sys import argv, exit
import argparse
import gzip
import numpy as np
from itertools import islice

try:
    vnum = open("VERSION.txt", 'r').readline().strip()
except:
    vnum = "0.2.0"
__version__ = "This is Fluidigm2PURC v"+vnum+"."

__header__ = """**********************************************
pacbio_err.py

Processing of FASTQ data from PacBio sequencing
to calculate grand mean level of sequencing error
for haplotype clustering.
**********************************************
"""

#### PHRED conversion dictionary. ##############################################

PHRED = {'!': 1.00, '"': 0.79433, '#': 0.63096, '$': 0.50119, '%': 0.39811,
         '&': 0.31623, '\'': 0.25119, '(': 0.19953, ')': 0.15849, '*': 0.12589,
         '+': 0.10000, ',': 0.07943, '-': 0.06310, '.': 0.05012, '/': 0.03981,
         '0': 0.03162, '1': 0.02512, '2': 0.01995, '3': 0.01585, '4': 0.01259,
         '5': 0.01000, '6': 0.00784, '7': 0.00631, '8': 0.00501, '9': 0.00398,
         ':': 0.00316, ';': 0.00251, '<': 0.00200, '=': 0.00158, '>': 0.00126,
         '?': 0.00100, '@': 0.00079, 'A': 0.00063, 'B': 0.00050, 'C': 0.00040,
         'D': 0.00032, 'E': 0.00025, 'F': 0.00020, 'G': 0.00016, 'H': 0.00013,
         'I': 0.00010, 'J': 0.00008, 'K': 0.00006, 'L': 0.00006, 'M': 0.00006,
         'N': 0.00006, 'O': 0.00006, 'P': 0.00006, 'Q': 0.00006, 'R': 0.00006,
         'S': 0.00006, 'T': 0.00006, 'U': 0.00006, 'V': 0.00006, 'W': 0.00006,
         'X': 0.00006, 'Y': 0.00006, 'Z': 0.00006}

def convert_phred(phred_string):
    """
    Convert a string of PHRED qulity scores to probabilities and take the mean.
    """
    if phred_string[-1] == '\n':
        return np.mean([PHRED[s] for s in phred_string[:-1]])
    else:
        return np.mean([PHRED[s] for s in phred_string])

def mean_err_per_read(in_handle):
    """
    Calculate the mean level of sequencing error per read and return as a list.
    """
    #for line in islice(in_handle, 3, None, 4):
    #	print(line)
    mean_err_list = [convert_phred(l) for l in islice(in_handle, 3, None, 4)]    
    return mean_err_list

def read_fastq(fastq):
	"""
	Read in FASTQ file, determine if it is gzipped, calculate the mean level of sequencing
	error per read (using mean_err_per_read fxn) and return the grand mean.
	"""
	gzipped    = False
	grand_mean = 0.0
	if fastq[-3:] == ".gz":
		gzipped = True

	if gzipped:
		with gzip.open(fastq, 'r') as f_in:
			mean_err = mean_err_per_read(f_in)
			grand_mean = np.mean(mean_err)
	else:
		with open(fastq) as f_in:
			mean_err = mean_err_per_read(f_in)
			grand_mean = np.mean(mean_err)
  
	return grand_mean
  		
if __name__ == "__main__":
	"""
	Parse command line arguments and run script.
	"""
	if len(argv) < 2:
		print(__doc__)
		exit(0)

	parser = argparse.ArgumentParser("Options for pacbio_err.py",
									 add_help=True)
	parser.add_argument('-v', '--version', action="version",
						  version=__version__)
	required = parser.add_argument_group("required arguments")
	required.add_argument('-i', '--infile', action="store", required=True,
						  metavar='\b', help="name of input FASTQ file.")
	
	args = parser.parse_args()
	infile = args.infile
	
	print("\n", __header__, sep="")
	
	print("Calculating grand mean level of sequencing error in file \'", infile, "\'...", sep='')
	grand_mean = read_fastq(infile)
	print("\nGrand mean:", grand_mean, "\n", sep='\t')
	
