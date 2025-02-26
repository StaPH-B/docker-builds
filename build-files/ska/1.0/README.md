# SKA container

Main tool : [SKA](https://github.com/simonrharris/SKA) 1.0

Additional tools:

- [generate_ska_alignment.py](https://github.com/nickjcroucher/gubbins/blob/master/python/scripts/generate_ska_alignment.py) 3.3
- python 3.5.1-3

Full documentation: [https://github.com/simonrharris/SKA/wiki](https://github.com/simonrharris/SKA/wiki)

SKA (Split Kmer Analysis) is a toolkit for prokaryotic (and any other small, haploid) DNA sequence analysis using split kmers. A split kmer is a pair of kmers in a DNA sequence that are separated by a single base. Split kmers allow rapid comparison and alignment of small genomes, and is particulalry suited for surveillance or outbreak investigation.SKA can produce split kmer files from fasta format assemblies or directly from fastq format read sequences, cluster them, align them with or without a reference sequence and provide various comparison and summary statistics. Currently all testing has been carried out on high-quality Illumina read data, so results for other platforms may vary.

## Basic usage - Rapid reference based whole genome alignment
#### 1 - Create list of input files
```
for f in *fna; do echo "${f%.fna}    ${f}"; done > input_list.txt
```

#### 2 - Create alignment
```
python3 generate_ska_alignment.py --reference cdip_reference.fasta --fasta input_list.txt --out cdip.aln
```
