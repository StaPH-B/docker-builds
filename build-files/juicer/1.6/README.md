# Juicer

Main tool: [Juicer](https://github.com/aidenlab/juicer)

Full documentation: https://github.com/aidenlab/juicer/wiki

> Juicer is a one-click pipeline for processing terabase scale Hi-C datasets.

Additional tools:

 * bwa 0.7.19
 * samtools 1.24
 * openjdk 21.0.12
 * python 3.12.3

## Example Usage

```
# ( put *_R1.fastq.gz and *_R2.fastq.gz at `fastq/` )

# build index
bwa index reference.fna
# prepare restriction site and chrom.sizes file
python /opt/juicer/misc/generate_site_positions.py DpnII reference.fna reference.fna
awk -vOFS=\\t '{print $1,$NF}' reference.fna_DpnII.txt > reference.fna.chrom.sizes
# run juicer.sh
juicer.sh -z reference.fna -y reference.fna_DpnII.txt -p reference.fna.chrom.sizes

# result will be located at `aligned/`
ls -al aligned
```
