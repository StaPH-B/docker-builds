# CFSAN SNP Pipeline

CFSAN SNP Pipeline [v2.2.1](https://github.com/CFSAN-Biostatistics/snp-pipeline/tree/v2.2.1)

## About
For producing SNP matrices from sequencing data for phylogenetic analysis of closely-related pathogenic organisms of interest to food safety. Pipeline was developed by the United States Food and Drug Administration, Center for Food Safety and Applied Nutrition.

## Usage
The all-in-one `cfsan_snp_pipeline run` command will perfrom alignment, variant calling, and SNP matrix generation given a reference FASTA file and sample FASTQ files for groups of related organisms.

Given the following example directory structure for the inputs:
```
/data/example/reference/reference.fasta
/data/example/samples/sample1/sample1_1.fastq
/data/example/samples/sample1/sample1_2.fastq
/data/example/samples/sample2/sample2_1.fastq
/data/example/samples/sample2/sample2_2.fastq
...
```

In the `example` directory, run the pipeline: 
```
bashcfsan_snp_pipeline run -s samples reference/reference.fasta
```

Full documentation for the pipeline can be found here: https://snp-pipeline.readthedocs.io/en/latest/readme.html

This Dockerfile is based on a Dockerfile by Justin Payne: https://github.com/CFSAN-Biostatistics/snp-pipeline/blob/v2.2.1/Dockerfile
