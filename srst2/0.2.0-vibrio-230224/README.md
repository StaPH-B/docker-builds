# SRST2 container

Main tool : [SRST2](https://github.com/katholt/srst2) 0.2.0

Additional tools:

- Biopython 1.76
- [Bowtie2](https://github.com/BenLangmead/bowtie2) 2.2.6-2
- python 2.7
- [SAMtools](https://github.com/samtools/samtools) 0.1.18
- SciPy 0.16

Full documentation: [https://github.com/katholt/srst2](https://github.com/katholt/srst2)

SRST2 performs short read sequence typing for bacterial pathogens when given Illumina sequence data, a MLST database, and/or a database of gene sequences  such as resistance genes, virulence genes, etc.)

## Custom *Vibrio cholerae* database info

This docker image includes a *Vibrio cholerae-specific* database of gene targets (traditionally used in PCR methods) for detecting O1 & O139 serotypes, toxin-production markers, and Biotype markers within the O1 serogroup ("El Tor" or "Classical" biotypes). These sequences were shared via personal communication with Dr. Christine Lee, of the National Listeria, Yersinia, Vibrio and Enterobacterales Reference Laboratory within the Enteric Diseases Laboratory Branch at CDC.

The genes included (and their purpose) included in the database are as follows:

- `ctxA` - Cholera toxin, an indication of toxigenic cholerae
- `ompW` - outer membrane protein, a *V. cholerae* species marker (alleles distinguishes *V. cholerae* from *V. parahaemolyticus* and *V. vulnificus*)
- `tcpA` - toxin co-pilus A, used to infer Biotype, either "El Tor" or "Clasical"
  - database includes an allele for each Biotype. `tcpA_classical` and `tcpA_ElTor`
- `toxR` - transcriptional activator (controls cholera toxin, pilus, and outer-membrane protein expression) - Species marker (allele distinguishes *V. cholerae* from *V. parahaemolyticus* and *V. vulnificus*)
- `wbeN` - O antigen encoding region - used to identify the O1 serogroup
- `wbfR` - O antigen encoding region - used to identify the O139 serogroup

The database's FASTA file & index files are located within `/vibrio-cholerae-db/` in the container's file system and can be utilized via the example command below.

## Basic usage - MLST

### 1 - Gather your input files

```bash
getmlst.py --species 'Escherichia coli#1'
```

### 2 - Run MLST

```bash
srst2 --input_pe strainA_1.fastq.gz strainA_2.fastq.gz --output strainA_test --log --mlst_db Escherichia_coli#1.fasta --mlst_definitions profiles_csv --mlst_delimiter _
```

### 3 - Check the outputs

MLST results are output in: `strainA_test__mlst__Escherichia_coli#1__results.txt`

## Basic usage - Vibrio characterization

### 1 - Run srst2

```bash
srst2 --input_pe strainA_1.fastq.gz strainA_2.fastq.gz --gene_db /vibrio-cholerae-db/vibrio_230224.fasta --output strainA_test
```

### 2 - Check the outputs

MLST results are output in: `strainA_test__genes__vibrio_230224__results.txt`
