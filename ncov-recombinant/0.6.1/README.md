# ncov-recombinant container

Main tool : [ncov-recombinant](https://github.com/ktmeaton/ncov-recombinant)

ncov-recombinant is a recombinant sequence detection tool for SARS-CoV-2 fasta files.
This tool:
1) Aligns sequences and performs clade/lineage assignments with Nextclade
2) Identifies parental clades and plots recombination breakpoints with sc2rf.
3) Creates tables, plots, and powerpoint slides for reporting.

## Example Usage

```bash
snakemake --profile /ncov-recombinant/profiles/controls
```
