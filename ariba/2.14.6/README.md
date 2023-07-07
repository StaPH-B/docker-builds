# ARIBA container

GitHub Repo: [ARIBA](https://github.com/sanger-pathogens/ariba)

Full documentation: [https://github.com/sanger-pathogens/ariba/wiki](https://github.com/sanger-pathogens/ariba/wiki)

Antimicrobial Resistance Identification By Assembly

ARIBA is a tool that identifies antibiotic resistance genes by running local assemblies. It can also be used for MLST calling.

The input is a FASTA file of reference sequences (can be a mix of genes and noncoding sequences) and paired sequencing reads. ARIBA reports which of the reference sequences were found, plus detailed information on the quality of the assemblies and any variants between the sequencing reads and the reference sequences.

## Example Usage

```
usage: ariba <command> <options>

optional arguments:
  -h, --help      show this help message and exit

Available commands:

aln2meta      Converts multi-aln fasta and SNPs to metadata
expandflag    Expands flag column of report file
flag          Translate the meaning of a flag
getref        Download reference data
micplot       Make violin/dot plots using MIC data
prepareref    Prepare reference data for input to "run"
pubmlstget    Download species from PubMLST and make db
pubmlstspecies
	      Get list of available species from PubMLST
refquery      Get cluster or sequence info from prepareref output
run           Run the local assembly pipeline
summary       Summarise multiple reports made by "run"
test          Run small built-in test dataset
version       Get versions and exit
```
Please read the [ARIBA wiki page](https://github.com/sanger-pathogens/ariba/wiki) for full usage instructions.