# ShigEiFinder docker image

Main tool : [ShigEiFinder](https://github.com/LanLab/ShigEiFinder)

Additional tools:

- bwa 0.7.17
- samtools 1.10
- python 3.8.10
- ncbi-blast+ 2.9.0

Full documentation: https://github.com/LanLab/ShigEiFinder

Publication: https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.000704

> This is a tool that is used to identify differentiate Shigella/EIEC using cluster-specific genes and identify the serotype using O-antigen/H-antigen genes. This pipeline can serotype over 59 Shigella and 22 EIEC serotypes using either assembled whole genomes or Whole Genome Sequencing (WGS) reads. The results are output in a tabular format which if saved as a file can be opened in Excel or other tabular programs.

## Example Usage

```bash
# genome assembly FASTA as input
$ shigeifinder -i GCF_000006925.2 \
      --hits \
      -t 2 \
      --output shigeifinder.GCF_000006925.2.out

$ head -n 2 shigeifinder.GCF_000006925.2.out 
#SAMPLE ipaH    VIRULENCE_PLASMID       CLUSTER SEROTYPE        O_ANTIGEN       H_ANTIGEN       NOTES
GCF_000006925   +       38      C3      SF2a    SF1-5

##############################################################

# paired end Illumina read FASTQs as input
$ shigeifinder -r \
      -i SRR21205791_1.fastq.gz  SRR21205791_2.fastq.gz \
      --hits \
      --dratio \
      -t 2 \
      --output shigeifinder.SRR21205791.out

$ head -n 2 shigeifinder.SRR21205791.out
#SAMPLE ipaH    VIRULENCE_PLASMID       CLUSTER SEROTYPE        O_ANTIGEN       H_ANTIGEN       NOTES
SRR21205791     +       38      CSS     SS      SS

# single end Illumina read FASTQs as input
$ shigeifinder -r \
      -i SRR21205791_1.fastq.gz  \
      --hits \
      --dratio \
      --single_end \
      -t 2 \
      --output shigeifinder.SRR21205791.single-end.out

$ head -n 2 shigeifinder.SRR21205791.single-end.out
#SAMPLE ipaH    VIRULENCE_PLASMID       CLUSTER SEROTYPE        O_ANTIGEN       H_ANTIGEN       NOTES
SRR21205791_1   +       38      CSS     SS      SS
```
