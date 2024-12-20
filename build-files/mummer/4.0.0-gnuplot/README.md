# mummer + RGDv2 container

Main tool : [mummer](https://github.com/mummer4/mummer)

Additional tools:

- `mash` v2.3
- `ani-m.pl` v0.1 from [https://github.com/lskatz/ani-m](https://github.com/lskatz/ani-m)
- `gnu-plot` v5.2 patchlevel 8
- `datasets` 14.17.0

MUMmer is a versatile alignment tool for DNA and protein sequences.

This docker image contains the **Reference Genome Database version 2 (RGDv2)** from the Enteric Diseases Laboratory Branch at the CDC. It contains the reference genomes of 43 enteric bacterial isolates that are used to for species identification of bacterial isolate WGS data. This database is NOT meant to be comprehensive - it contains the genomes of enteric pathogens commonly sequenced by EDLB and some closely related species. Here is the publication describing the database: [https://doi.org/10.3389/fmicb.2023.1225207](https://doi.org/10.3389/fmicb.2023.1225207)

The FASTA files for RGDv2 can be found within the directory `/RGDv2/` inside the docker image.

The docker image also includes `ani-m.pl`, written by [Lee Katz](@lskatz) and Lori Gladney. This perl script can be used for running the `dnadiff` tool from the Mummer package for performing Average Nucleotide Identity (ANI) analysis to compare genomes.

## Example Usage

Compare one genome against the 43 genomes in RGDv2, writing the output to a TSV file.

This script will automatically use `mash` as quick check to see relatedness between genomes. If the two genomes have less than 0.9 mash distance, then the ANI calculation will be skipped.

The `--symmetric` flag will run ANI comparison on both:

 1. the query vs the reference genome, followed by...
 2. the reference versus the query genome.

 ANI values will likely be nearly identical between the two comparisons, but differences may occur in the `percentAligned` or percent bases aligned value depending on the sequences present in the genome.

```bash
ani-m.pl --symmetric --mash-filter 0.9 my-assembly-of-interest.fasta /RGDv2/*.fasta | tee output.tsv
```

Example output TSV when comparing a Salmonella enterica serotype Kentucky to RGDv2 using the above command:

```bash
$ column -t output-with-mash-and-symmetric-flag.tsv 
reference                                     query                                         ANI      stdev  percentAligned
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_000026225.1.Escherichia_fergusonii.fasta  84.7423  3.93   33.1834
GCA_000026225.1.Escherichia_fergusonii.fasta  GCA_011245895.1_PDT000672941.1_genomic.fna    84.7485  3.97   35.6278
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_000512125.1.Escherichia_albertii.fasta    84.8404  3.72   32.5365
GCA_000512125.1.Escherichia_albertii.fasta    GCA_011245895.1_PDT000672941.1_genomic.fna    84.8391  3.72   34.8883
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_002741475.1.Escherichia_coli.fasta        84.7711  3.76   35.5718
GCA_002741475.1.Escherichia_coli.fasta        GCA_011245895.1_PDT000672941.1_genomic.fna    84.7762  3.76   35.8077
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_009665195.1.Vibrio_mimicus.fasta          89.4273  6.41   0.7529
GCA_009665195.1.Vibrio_mimicus.fasta          GCA_011245895.1_PDT000672941.1_genomic.fna    89.4215  6.40   1.5694
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_009665515.2.Vibrio_cholerae.fasta         93.7723  7.47   2.4096
GCA_009665515.2.Vibrio_cholerae.fasta         GCA_011245895.1_PDT000672941.1_genomic.fna    93.7724  7.52   3.0205
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_011388235.1.Salmonella_enterica.fasta     98.7341  3.42   88.7485
GCA_011388235.1.Salmonella_enterica.fasta     GCA_011245895.1_PDT000672941.1_genomic.fna    98.7335  2.79   94.5892
GCA_011245895.1_PDT000672941.1_genomic.fna    GCA_013588055.1.Salmonella_bongori.fasta      90.3425  2.99   73.3307
GCA_013588055.1.Salmonella_bongori.fasta      GCA_011245895.1_PDT000672941.1_genomic.fna    90.3405  2.95   81.9293
```

Better documentation for Mummer can be found at [https://github.com/mummer4/mummer](https://github.com/mummer4/mummer)

A tutorial can be found at [https://mummer4.github.io/tutorial/tutorial.html](https://mummer4.github.io/tutorial/tutorial.html)

And the manual can be found at [http://mummer.sourceforge.net/manual/](http://mummer.sourceforge.net/manual/)
