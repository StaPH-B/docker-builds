# ARIBA container

Main tool: [ARIBA](https://github.com/sanger-pathogens/ariba)

Additional tools:
- [pysam](https://github.com/pysam-developers/pysam) 0.15.4
- [SPAdes](https://github.com/ablab/spades) 3.15.5

Full documentation: [https://github.com/sanger-pathogens/ariba/wiki](https://github.com/sanger-pathogens/ariba/wiki)

Antimicrobial Resistance Identification By Assembly

ARIBA is a tool that identifies antibiotic resistance genes by running local assemblies. It can also be used for MLST calling.

The input is a FASTA file of reference sequences (can be a mix of genes and noncoding sequences) and paired sequencing reads. ARIBA reports which of the reference sequences were found, plus detailed information on the quality of the assemblies and any variants between the sequencing reads and the reference sequences.

## Example Usage

```bash
# Get reference data, for instance from CARD
ariba getref ncbi out.ncbi

# Prepare reference data for ARIBA
ariba prepareref -f out.ncbi.fa -m out.ncbi.tsv out.ncbi.prepareref

# Run local assemblies and call variants
ariba run out.ncbi.prepareref reads1.fastq reads2.fastq out.run

#Summarise data from several runs
ariba summary out.summary out.run1/report1.tsv out.run2/report2.tsv out.run3/report3.tsv
```
Please read the [ARIBA wiki page](https://github.com/sanger-pathogens/ariba/wiki) for full usage instructions.