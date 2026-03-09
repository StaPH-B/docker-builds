# Hifiasm container

Main tool: [hifiasm](https://github.com/chhylp123/hifiasm)
  
Code repository: https://github.com/chhylp123/hifiasm

Additional tools:
- yak: 0.1 (r56)

Basic information on how to use this tool:
- executable: `hifiasm`
- help: `-h`
- version: `--version`
- description: 
>Hifiasm is a fast haplotype-resolved de novo assembler initially designed for PacBio HiFi reads. Its latest release could support the telomere-to-telomere assembly by utilizing ultralong Oxford Nanopore reads.

Additional information:

Cheng, H., Concepcion, G.T., Feng, X., Zhang, H., Li H. (2021) Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm. Nat Methods, 18:170-175. https://doi.org/10.1038/s41592-020-01056-5
  
Full documentation: https://hifiasm.readthedocs.io/en/latest/index.html

## Example Usage

```bash
# Run on test data (use -f0 for small datasets)
wget https://github.com/chhylp123/hifiasm/releases/download/v0.7/chr11-2M.fa.gz
./hifiasm -o test -t4 -f0 chr11-2M.fa.gz 2> test.log
awk '/^S/{print ">"$2;print $3}' test.bp.p_ctg.gfa > test.p_ctg.fa  # get primary contigs in FASTA

# Assemble inbred/homozygous genomes (-l0 disables duplication purging)
hifiasm -o CHM13.asm -t32 -l0 CHM13-HiFi.fa.gz 2> CHM13.asm.log
# Assemble heterozygous genomes with built-in duplication purging
hifiasm -o HG002.asm -t32 HG002-file1.fq.gz HG002-file2.fq.gz

# Assemble genomes with ONT R10 reads rather than PacBio HiFi reads using the latest release of hifiasm (>0.21.0-r686)
hifiasm -o HG002.asm --ont -t32 HG002-ont.fq.gz

# Hi-C phasing with paired-end short reads in two FASTQ files
hifiasm -o HG002.asm --h1 read1.fq.gz --h2 read2.fq.gz HG002-HiFi.fq.gz

# Trio binning assembly (requiring https://github.com/lh3/yak)
yak count -b37 -t16 -o pat.yak <(cat pat_1.fq.gz pat_2.fq.gz) <(cat pat_1.fq.gz pat_2.fq.gz)
yak count -b37 -t16 -o mat.yak <(cat mat_1.fq.gz mat_2.fq.gz) <(cat mat_1.fq.gz mat_2.fq.gz)
hifiasm -o HG002.asm -t32 -1 pat.yak -2 mat.yak HG002-HiFi.fa.gz

# Improve contiguity for diploid genome assembly by self-scaffolding (`--dual-scaf`)
hifiasm -o HG002.asm --dual-scaf --h1 read1.fq.gz --h2 read2.fq.gz HG002-HiFi.fq.gz

# Preserve more telomeres for human genomes (`--telo-m CCCTAA`)
hifiasm -o HG002.asm --telo-m CCCTAA --h1 read1.fq.gz --h2 read2.fq.gz HG002-HiFi.fq.gz

# Hybrid assembly with HiFi, ultralong and Hi-C reads
hifiasm -o HG002.asm --h1 read1.fq.gz --h2 read2.fq.gz --ul ul.fq.gz HG002-HiFi.fq.gz

# Single-sample telomere-to-telomere assembly for diploid human genomes
hifiasm -o HG002.asm --dual-scaf --telo-m CCCTAA --h1 read1.fq.gz --h2 read2.fq.gz --ul ul.fq.gz HG002-HiFi.fq.gz
```
