# SRST2 container

Main tool : [SRST2](https://github.com/katholt/srst2) 0.2.0

Additional tools:

- Biopython 1.76
- [Bowtie2](https://github.com/BenLangmead/bowtie2) 2.2.6-2
- python 2.7
-[SAMtools](https://github.com/samtools/samtools) 0.1.18
- SciPy 0.16



Full documentation: [https://github.com/katholt/srst2](https://github.com/katholt/srst2)

SRST2  performs short read sequence typing for bacterial pathogens when given Illumina sequence data, a MLST database, and/or a database of gene sequences  such as resistance genes, virulence genes, etc.)



## Basic usage - MLST

#### 1 - Gather your input files

(i) sequence reads (this example uses paired reads in gzipped fastq format, see below for options)

(ii) a fasta sequence database to match to. For MLST, this means a fasta file of all allele sequences. If you want to assign STs, you also need a tab-delim file which defines the ST profiles as a combination of alleles. You can retrieve these files automatically from pubmlst.org/data/ using the script provided:

```
getmlst.py --species 'Escherichia coli#1'
```

#### 2 - Run MLST

```
srst2 --input_pe strainA_1.fastq.gz strainA_2.fastq.gz --output strainA_test --log --mlst_db Escherichia_coli#1.fasta --mlst_definitions profiles_csv --mlst_delimiter _
```

#### 3 - Check the outputs

(i) MLST results are output in: `strainA_test__mlst__Escherichia_coli#1__results.txt`

Sample | ST | adk | fumC | gyrB | icd | mdh | purA | recA | mismatches | uncertainty | depth | maxMAF
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
strainA | 152 | 11 | 63 | 7 | 1 | 14 | 7 | 7 | 0 | - | 25.8319955826 | 0.125
