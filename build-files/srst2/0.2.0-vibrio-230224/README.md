# SRST2 container

Main tool : [SRST2](https://github.com/katholt/srst2) 0.2.0

Additional tools:

- Biopython 1.76
- [Bowtie2](https://github.com/BenLangmead/bowtie2) 2.2.6-2
- python 2.7
- [SAMtools](https://github.com/samtools/samtools) 0.1.18
- SciPy 0.16

Full documentation: [https://github.com/katholt/srst2](https://github.com/katholt/srst2)

SRST2 performs short read sequence typing for bacterial pathogens when given Illumina sequence data, a MLST database, and/or a database of gene sequences  such as resistance genes, virulence genes, etc.

## Custom *Vibrio cholerae* database info

This docker image includes a *Vibrio cholerae-specific* database of gene targets (traditionally used in PCR methods) for detecting O1 & O139 serotypes, toxin-production markers, and Biotype markers within the O1 serogroup ("El Tor" or "Classical" biotypes). These sequences were shared via personal communication with Dr. Christine Lee, of the National Listeria, Yersinia, Vibrio and Enterobacterales Reference Laboratory within the Enteric Diseases Laboratory Branch at CDC.

The genes included (and their purpose) included in the database are as follows:

- `ctxA` - Cholera toxin, an indication of toxigenic cholerae
- `ompW` - outer membrane protein, a *V. cholerae* species marker (presence of any allele of this gene distinguishes *V. cholerae* from *V. parahaemolyticus* and *V. vulnificus*)
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
srst2 --input_pe SRR7062495_1.fastq.gz SRR7062495_2.fastq.gz --gene_db /vibrio-cholerae-db/vibrio_230224.fasta --output SRR7062495_test
```

### 2 - Check the outputs

Summary results are output in: `SRR7062495_test__genes__vibrio_230224__results.txt` and detailed results are found in `SRR7062495_test__fullgenes__vibrio_230224__results.txt`

```bash
# summary
$ column -t -s $'\t' -n SRR7062495_test__genes__vibrio_230224__results.txt 
Sample      ctxA       ompW        tcpA_ElTor         toxR        wbeN_O1
SRR7062495  ctxA_O395  ompW_O395*  tcpA_ElTor_C6706*  toxR_O395*  wbeN_O1_INDRE

# detailed results
$ column -t -s $'\t' -n SRR7062495_test__fullgenes__vibrio_230224__results.txt
Sample      DB             gene        allele            coverage  depth    diffs  uncertainty  divergence  length  maxMAF  clusterid  seqid  annotation
SRR7062495  vibrio_230224  ctxA        ctxA_O395         100.0     103.877                      0.0         777     0.063   1          1      CP000627.1
SRR7062495  vibrio_230224  ompW        ompW_O395         100.0     78.414   6snp                0.917       654     0.04    2          3      CP000626.1
SRR7062495  vibrio_230224  toxR        toxR_O395         100.0     74.081   14snp               1.582       885     0.053   5          6      CP000627.1
SRR7062495  vibrio_230224  tcpA_ElTor  tcpA_ElTor_C6706  100.0     82.698   1snp                0.148       675     0.046   4          5      CP064350.1
SRR7062495  vibrio_230224  wbeN_O1     wbeN_O1_INDRE     100.0     112.119                      0.0         2478    0.091   6          7      
```
