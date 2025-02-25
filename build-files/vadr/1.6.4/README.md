# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

You can find [additional information on the SARS-CoV-2 models used by VADR here](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation#sarscov2models). Models can be downloaded from the [NCBI FTP server](https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/)

Additional tools:

- perl v5.22.1
- infernal v1.1.5
- ncbi-blast+ v2.15.0
- fasta v36.3.8h (the tool, not the file format)
- minimap2 v2.26

Note : Only the default 'calici', 'noro', and 'sarscov2' models are included in this image. Users are recommended to download their own models or use an alternative image.

### VADR Documentation

- [Full documentation](https://github.com/ncbi/vadr#vadr-documentation-)
- [Docs on Coronavirus annotation](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation)
- [Docs on Mpox annotation](https://github.com/ncbi/vadr/wiki/Mpox-virus-annotation)
- [Docs on Dengue and other Flaviviridae annotation](https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#dengue-virus-and-other-flaviviridae-refseq-vadr-models)
- [Docs on RSV annotation](https://github.com/ncbi/vadr/wiki/RSV-annotation)
- [Docs on flu annotation](https://github.com/ncbi/vadr/wiki/Influenza-annotation)

## Example Usage

```bash
# trim terminal Ns from my input genome (VADR requires this as the first step)
/opt/vadr/vadr/miniscripts/fasta-trim-terminal-ambigs.pl \
    /data/SRR13957123.consensus.fa \
    --minlen 50 \
    --maxlen 30000 \
    > /data/SRR13957123.consensus.trimmed.fasta
```
