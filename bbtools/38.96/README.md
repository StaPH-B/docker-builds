# BBTools container

Main tool : [BBTools](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/)

Additional tools:
- [BBDuk](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbduk-guide/): `bbduk.sh` (or `bbduk2.sh`)
- [BBMap](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmap-guide/): `bbmap.sh`
- [BBMerge](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmerge-guide/): `bbmerge.sh`
- [Reformat](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/reformat-guide/): `reformat.sh`

Full documentation: https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/

> BBTools is a suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data. BBTools can handle common sequencing file formats such as fastq, fasta, sam, scarf, fasta+qual, compressed or raw, with autodetection of quality encoding and interleaving. It is written in Java and works on any platform supporting Java, including Linux, MacOS, and Microsoft Windows and Linux; there are no dependencies other than Java (version 7 or higher). Program descriptions and options are shown when running the shell scripts with no parameters. 

# Example Usage

Interleave a pair of FASTQ files for downstream processing:

```
reformat.sh \
    in1=${SAMPLE}_R1.fastq.gz \
    in2=${SAMPLE}_R2.fastq.gz \
    out=${SAMPLE}.fastq.gz
```

Split into SARS-CoV-2 and non-SARS-CoV-2 reads:
```
bbduk.sh ow -Xmx1g \
    in=${SAMPLE}.fq.gz \
    ref=REFERENCE.fasta \
    outm=${SAMPLE}_viral.fq.gz \
    outu=${SAMPLE}_nonviral.fq.gz \
    k=25
```
