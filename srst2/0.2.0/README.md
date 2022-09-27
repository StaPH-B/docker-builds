# SRST2 container

Main tool : [SRST2](https://github.com/katholt/srst2) 0.2.0

Additional tools:

- Biopython 1.76
- [Bowtie2](https://github.com/BenLangmead/bowtie2) 2.2.6-2
- python 2.7
- [SAMtools](https://github.com/samtools/samtools) 0.1.18
- SciPy 0.16

Full documentation: [https://github.com/katholt/srst2](https://github.com/katholt/srst2)

SRST2  performs short read sequence typing for bacterial pathogens when given Illumina sequence data, a MLST database, and/or a database of gene sequences  such as resistance genes, virulence genes, etc.)

## Basic usage - MLST
#### 1 - Gather your input files
```
getmlst.py --species 'Escherichia coli#1'
```

#### 2 - Run MLST
```
srst2 --input_pe strainA_1.fastq.gz strainA_2.fastq.gz --output strainA_test --log --mlst_db Escherichia_coli#1.fasta --mlst_definitions profiles_csv --mlst_delimiter _
```

#### 3 - Check the outputs
MLST results are output in: `strainA_test__mlst__Escherichia_coli#1__results.txt`
