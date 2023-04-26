# minimap2 container

Main tool : [minimap2](https://github.com/lh3/minimap2)

Additional tools:

- none (apart from basic linux utilties included in `ubuntu:jammy` base docker image, like `ls`, `mkdir`, etc.) 

Publication: [https://academic.oup.com/bioinformatics/article/34/18/3094/4994778?login=false](https://academic.oup.com/bioinformatics/article/34/18/3094/4994778?login=false)

Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.

## Example Usage

These example commands were copy/pasted directly from: [https://github.com/lh3/minimap2#getting-started](https://github.com/lh3/minimap2#getting-started)

```bash
# use presets (no test data)
minimap2 -ax map-pb ref.fa pacbio.fq.gz > aln.sam       # PacBio CLR genomic reads
minimap2 -ax map-ont ref.fa ont.fq.gz > aln.sam         # Oxford Nanopore genomic reads
minimap2 -ax map-hifi ref.fa pacbio-ccs.fq.gz > aln.sam # PacBio HiFi/CCS genomic reads (v2.19 or later)
minimap2 -ax asm20 ref.fa pacbio-ccs.fq.gz > aln.sam    # PacBio HiFi/CCS genomic reads (v2.18 or earlier)
minimap2 -ax sr ref.fa read1.fa read2.fa > aln.sam      # short genomic paired-end reads
minimap2 -ax splice ref.fa rna-reads.fa > aln.sam       # spliced long reads (strand unknown)
minimap2 -ax splice -uf -k14 ref.fa reads.fa > aln.sam  # noisy Nanopore Direct RNA-seq
minimap2 -ax splice:hq -uf ref.fa query.fa > aln.sam    # Final PacBio Iso-seq or traditional cDNA
minimap2 -ax splice --junc-bed anno.bed12 ref.fa query.fa > aln.sam  # prioritize on annotated junctions
minimap2 -cx asm5 asm1.fa asm2.fa > aln.paf             # intra-species asm-to-asm alignment
minimap2 -x ava-pb reads.fa reads.fa > overlaps.paf     # PacBio read overlap
minimap2 -x ava-ont reads.fa reads.fa > overlaps.paf    # Nanopore read overlap
```
