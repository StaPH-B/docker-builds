# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

Included SARS-CoV-2 models version: 1.3-2

You can find [additional information on the SARS-CoV-2 models used by VADR here](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation#sarscov2models). The models are downloaded from the [NCBI FTP server](https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/)

Additional tools:

- perl
- infernal
- hmmer
- ncbi-blast+
- fasta (the tool, not the file format)

Full documentation: https://github.com/ncbi/vadr#vadr-documentation-

Docs on Coronavirus annotation: https://github.com/ncbi/vadr/wiki/Coronavirus-annotation

## Example Usage

```bash
# trim terminal Ns from my input genome (VADR requires this as the first step)
/opt/vadr/vadr/miniscripts/fasta-trim-terminal-ambigs.pl \
        /data/SRR13957123.consensus.fa \
        --minlen 50 \
        --maxlen 30000 \
        > /data/SRR13957123.consensus.trimmed.fasta

# run v-annotate.pl using the sarscov2 models to annotate my trimmed input genome
v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
       --mkey sarscov2 --lowsim5seq 6 \
       --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
       "/data/SRR13957123.consensus.trimmed.fasta" \
       "SRR13957123-vadr-outdir"
```
