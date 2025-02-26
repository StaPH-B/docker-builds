## BBTools

This image implements Brian Bushnell's [BBTools](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/).

### Includes
- [BBDuk](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbduk-guide/): `bbduk.sh` (or `bbduk2.sh`)
- [BBMap](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmap-guide/): `bbmap.sh`
- [BBMerge](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmerge-guide/): `bbmerge.sh`
- [Reformat](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/reformat-guide/): `reformat.sh`

To see all of the executables in this image, run the following command inside a container:

```text
ls /usr/local/bin
```

Documentation is in the `/opt/bbmap/docs/` directory, and in each tool's shell script in `/opt/bbmap/`.

### Example Usage
(adapted from `/opt/bbmap/pipelines/covid/processCorona.sh`)

Interleave a pair of FASTQ files for downstream processing:

```text
reformat.sh \
    in1=${SAMPLE}_R1.fastq.gz \
    in2=${SAMPLE}_R2.fastq.gz \
    out=${SAMPLE}.fastq.gz
```
Split into SARS-CoV-2 and non-SARS-CoV-2 reads:

```text
bbduk.sh ow -Xmx1g \
    in=${SAMPLE}.fq.gz \
    ref=REFERENCE.fasta \
    outm=${SAMPLE}_viral.fq.gz \
    outu=${SAMPLE}_nonviral.fq.gz \
    k=25
```
