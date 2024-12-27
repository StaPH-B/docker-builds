# bedtools2 container

GitHub Repo: [bedtools](https://github.com/arq5x/bedtools2/)

Full documentation: [https://bedtools.readthedocs.io/en/latest/index.html](https://bedtools.readthedocs.io/en/latest/index.html)

> Collectively, the bedtools utilities are a swiss-army knife of tools for a wide-range of genomics analysis tasks. The most widely-used tools enable genome arithmetic: that is, set theory on the genome. For example, bedtools allows one to intersect, merge, count, complement, and shuffle genomic intervals from multiple files in widely-used genomic file formats such as BAM, BED, GFF/GTF, VCF. While each individual tool is designed to do a relatively simple task (e.g., intersect two interval files), quite sophisticated analyses can be conducted by combining multiple bedtools operations on the UNIX command line.

List of sub-commands in bedtools 2.31.0:

- annotate
- bamtobed
- bamtofastq
- bed12tobed6
- bedpetobam
- bedtobam
- closest
- cluster
- complement
- coverage
- expand
- flank
- fisher
- genomecov
- getfasta
- groupby
- igv
- intersect
- jaccard
- links
- makewindows
- map
- maskfasta
- merge
- multicov
- multiinter
- nuc
- overlap
- pairtobed
- pairtopair
- random
- reldist
- shift
- shuffle
- slop
- sort
- subtract
- summary
- tag
- unionbedg
- window

## Example Usage

```bash
# bedtools consists of a suite of sub-commands that are invoked as follows:
# bedtools [sub-command] [options]

# For example, to intersect two BED files, one would invoke the following:
bedtools intersect -a a.bed -b b.bed
```

More examples are found in the [bedtools tutorial](http://quinlanlab.org/tutorials/bedtools/bedtools.html)
