# Shovill v1.1.0 docker image

Main tool : [Shovill](https://github.com/tseemann/shovill)

Additional tools:

- SPAdes 3.15.5
- SKESA 2.3.0
- megahit 1.1.4
- velvet 1.2.10
- seqtk 1.3
- kmc 3.1.1
- lighter 1.1.1
- trimmomatic 0.39
- bwa 0.7.17
- pilon 1.24
- samclip
- perl 5.22.1
- python 2.7.12
- pigz

Full documentation: [https://github.com/tseemann/shovill](https://github.com/tseemann/shovill)

> *Assemble bacterial isolate genomes from Illumina paired-end reads*

## NOTE ON DEC 2022 UPGRADES

The Shovill 1.1.0 docker image was originally developed in May 2020 using this the version of the dockerfile, [commit 615d1cfeb4](https://github.com/StaPH-B/docker-builds/blob/615d1cfeb464df4635b2efbe1b359351c5b5b0f7/shovill/1.1.0/Dockerfile)

This older docker image will be maintained under this docker image tag: `staphb/shovill:1.1.0`

The Shovill docker image has since been upgraded via [Pull Request #511](https://github.com/StaPH-B/docker-builds/pull/511) which upgraded the following tools in the shovill 1.1.0 dockerfile. Other smaller changes were also introduced (see the PR for details)

- upgraded spades from 3.14.1 to 3.15.5
- upgraded pilon from 1.22 to 1.24
- upgraded samtools from 1.10 to 1.16.1
- upgraded trimmomatic from 0.38 to 0.39

This newer docker image will be maintained under the docker image tags: `staphb/shovill:1.1.0-2022Dec` & `staphb/shovill:latest` in an effort to preserve the older docker image & allow for users to more easily transition to the new docker image in their pipelines.

### Example Usage

```bash
# run shovill on the test FASTQ files bundled with shovill
shovill --outdir /data/out.spades --assembler spades --R1 /shovill-1.1.0/test/R1.fq.gz --R2 /shovill-1.1.0/test/R2.fq.gz
```
