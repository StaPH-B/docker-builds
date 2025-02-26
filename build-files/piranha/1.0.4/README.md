# piranha 1.0.4 container

Main tool : [piranha](https://github.com/polio-nanopore/piranha)

Full documentation: [https://github.com/polio-nanopore/piranha](https://github.com/polio-nanopore/piranha)

> Poliovirus Investigation Resource Automating Nanopore Haplotype Analysis. <br><br> piranha is a tool in development as part of the Poliovirus Sequencing Consortium. It runs an automated analysis pipeline for sequencing VP1 regions of the poliovirus or non-polio enterovirus genome (whole genome analysis to be implemented soon) and produces an interactive report alongside the consensus data.

Additional tools:

- [samtools/bcftools/tabix](https://github.com/samtools/samtools) 1.11
- [minimap2](https://github.com/lh3/minimap2) 2.17
- [gofasta](https://github.com/virus-evolution/gofasta) 1.1.0
- [mafft](https://mafft.cbrc.jp/alignment/software/) 7.508
- [racon](https://github.com/isovic/racon) 1.5.0
- [medaka](https://github.com/nanoporetech/medaka) 1.7.2
- python 3.9.9
- biopython 1.79
- snakemake-minimal 7.17.1

## Example Usage

```bash
# run Piranha on a directory of FASTQs (Guppy output)
piranha -i /piranha/test/pak_run/demultiplexed --verbose -b piranha/test/pak_run/barcodes01.csv -t 2 2>&1 | tee piranha.log
```
