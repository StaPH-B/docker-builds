# Prokka

This image implements the prokaryotic genome annotation tool [Prokka](https://github.com/tseemann/prokka).
Documentation is available at https://github.com/tseemann/prokka. 

Prokka databases are in `/prokka-1.14.5/db` and include:
* Kingdoms: Archaea Bacteria Mitochondria Viruses
* Genera: Enterococcus Escherichia Staphylococcus
* HMMs: HAMAP
* CMs: Archaea Bacteria Viruses

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (a bacterial genome assembly)
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# Run program to annotate a genome assembly with option: --addgenes Add 'gene' features for each 'CDS' feature
prokka \
  --outdir results \
  --prefix test \
  --addgenes \
  NCTC13799.fna
```

## Example output

The on-screen output tells you what the program did and what files it generated:
```
[10:17:17] This is prokka 1.14.5
[10:17:17] Written by Torsten Seemann <torsten.seemann@gmail.com>
[10:17:17] Homepage is https://github.com/tseemann/prokka
[10:17:17] Local time is Mon Apr 25 10:17:17 2022
[10:17:17] You are not telling me who you are!
[10:17:17] Operating system is linux
[10:17:17] You have BioPerl 1.006924
[10:17:17] System has 3 cores.
[10:17:17] Option --cpu asked for 8 cores, but system only has 3
[10:17:17] Will use maximum of 3 cores.
[10:17:17] Annotating as >>> Bacteria <<<
[10:17:17] Generating locus_tag from 'NCTC13799.fna' contents.
[10:17:17] Setting --locustag EELFEJCC from MD5 ee5fe3cc154da9697c0cc947c49511e6
[10:17:17] Creating new output folder: results
[10:17:17] Running: mkdir -p results
[10:17:17] Using filename prefix: test.XXX
[10:17:17] Setting HMMER_NCPU=1
[10:17:17] Writing log to: results/test.log
[10:17:17] Command: /prokka-1.14.5/bin/prokka --outdir results --prefix test --addgenes NCTC13799.fna
...
[10:17:18] Using genetic code table 11.
[10:17:18] Loading and checking input file: NCTC13799.fna
[10:17:18] Wrote 1 contigs totalling 2172222 bp.
[10:17:18] Predicting tRNAs and tmRNAs
[10:17:18] Running: aragorn -l -gc11  -w results\/test\.fna
[10:17:19] 1 tRNA-Leu c[13586,13671] 35 (gag)
[10:17:19] 2 tRNA-Lys [58617,58692] 34 (ttt)
...
[10:17:19] Found 58 tRNAs
[10:17:19] Predicting Ribosomal RNAs
[10:17:19] Running Barrnap with 3 threads
[10:17:23] 1 NZ_LT906437.1 1201554 5S ribosomal RNA
[10:17:23] 2 NZ_LT906437.1 1201762 23S ribosomal RNA
...
[10:17:23] Found 12 rRNAs
[10:17:23] Skipping ncRNA search, enable with --rfam if desired.
[10:17:23] Total of 69 tRNA + rRNA features
[10:17:23] Searching for CRISPR repeats
[10:17:24] Found 0 CRISPRs
[10:17:24] Predicting coding sequences
[10:17:24] Contigs total 2172222 bp, so using single mode
[10:17:24] Running: prodigal -i results\/test\.fna -c -m -g 11 -p single -f sco -q
[10:17:31] Excluding CDS which overlaps existing RNA (rRNA) at NZ_LT906437.1:1201911..1202561 on + strand
...
[10:17:32] Found 2160 CDS
[10:17:32] Connecting features back to sequences
[10:17:32] Not using genus-specific database. Try --usegenus to enable it.
[10:17:32] Annotating CDS, please be patient.
[10:17:32] Will use 3 CPUs for similarity searching.
[10:17:35] There are still 2160 unannotated CDS left (started with 2160)
[10:17:35] Will use blast to search against /prokka-1.14.5/db/kingdom/Bacteria/IS with 3 CPUs
[10:17:35] Running: cat results\/test\.IS\.tmp\.12\.faa | parallel --gnu --plain -j 3 --block 102255 --recstart '>' --pipe blastp -query - -db /prokka-1.14.5/db/kingdom/Bacteria/IS -evalue 1e-30 -qcov_hsp_perc 90 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > results\/test\.IS\.tmp\.12\.blast 2> /dev/null
[10:18:02] Deleting unwanted file: results/test.IS.tmp.12.faa
[10:18:02] Deleting unwanted file: results/test.IS.tmp.12.blast
[10:18:04] There are still 2124 unannotated CDS left (started with 2160)
[10:18:04] Will use blast to search against /prokka-1.14.5/db/kingdom/Bacteria/AMR with 3 CPUs
[10:18:04] Running: cat results\/test\.AMR\.tmp\.12\.faa | parallel --gnu --plain -j 3 --block 100959 --recstart '>' --pipe blastp -query - -db /prokka-1.14.5/db/kingdom/Bacteria/AMR -evalue 9.99999999999999e-301 -qcov_hsp_perc 90 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > results\/test\.AMR\.tmp\.12\.blast 2> /dev/null
[10:18:20] Deleting unwanted file: results/test.AMR.tmp.12.faa
[10:18:20] Deleting unwanted file: results/test.AMR.tmp.12.blast
[10:18:23] There are still 2124 unannotated CDS left (started with 2160)
[10:18:23] Will use blast to search against /prokka-1.14.5/db/kingdom/Bacteria/sprot with 3 CPUs
[10:18:23] Running: cat results\/test\.sprot\.tmp\.12\.faa | parallel --gnu --plain -j 3 --block 100959 --recstart '>' --pipe blastp -query - -db /prokka-1.14.5/db/kingdom/Bacteria/sprot -evalue 1e-09 -qcov_hsp_perc 80 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > results\/test\.sprot\.tmp\.12\.blast 2> /dev/null
[10:19:35] Modify product: UPF0701 protein HI_0467 => hypothetical protein
...
[10:20:16] Found 1053 unique /gene codes.
[10:20:16] Fixed 2 duplicate /gene - mnmC_1 mnmC_2
...
[10:20:16] Fixed 69 colliding /gene names.
[10:20:16] Adding /locus_tag identifiers
[10:20:16] Assigned 2230 locus_tags to CDS and RNA features.
[10:20:16] Writing outputs to results/
[10:20:21] Generating annotation statistics file
[10:20:21] Generating Genbank and Sequin files
[10:20:21] Running: tbl2asn -V b -a r10k -l paired-ends -M n -N 1 -y 'Annotated using prokka 1.14.5 from https://github.com/tseemann/prokka' -Z results\/test\.err -i results\/test\.fsa 2> /dev/null
[10:20:28] Deleting unwanted file: results/errorsummary.val
[10:20:28] Deleting unwanted file: results/test.dr
[10:20:28] Deleting unwanted file: results/test.fixedproducts
[10:20:28] Deleting unwanted file: results/test.ecn
[10:20:28] Deleting unwanted file: results/test.val
[10:20:28] Repairing broken .GBK output that tbl2asn produces...
[10:20:28] Running: sed 's/COORDINATES: profile/COORDINATES:profile/' < results\/test\.gbf > results\/test\.gbk
[10:20:28] Deleting unwanted file: results/test.gbf
[10:20:28] Output files:
[10:20:28] results/test.tbl
[10:20:28] results/test.gbk
[10:20:28] results/test.fsa
[10:20:28] results/test.faa
[10:20:28] results/test.sqn
[10:20:28] results/test.ffn
[10:20:28] results/test.tsv
[10:20:28] results/test.txt
[10:20:28] results/test.err
[10:20:28] results/test.fna
[10:20:28] results/test.gff
[10:20:28] results/test.log
[10:20:28] Annotation finished successfully.
[10:20:28] Walltime used: 3.18 minutes
[10:20:28] If you use this result please cite the Prokka paper:
[10:20:28] Seemann T (2014) Prokka: rapid prokaryotic genome annotation. Bioinformatics. 30(14):2068-9.
[10:20:28] Type 'prokka --citation' for more details.
[10:20:28] Share and enjoy!
```