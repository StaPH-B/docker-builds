# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

You can find [additional information on the SARS-CoV-2 models used by VADR here](https://github.com/ncbi/vadr/wiki/Coronavirus-annotation#sarscov2models). The models are downloaded from the [NCBI FTP server](https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/)

Additional tools:

- perl v5.22.1
- infernal v1.1.5
- ncbi-blast+ v2.15.0
- fasta v36.3.8h (the tool, not the file format)
- minimap2 v2.26

Available VADR models:
- Norovirus and other Caliciviridae
- Dengue virus and other Flaviviridae

Additional VADR models:

- HAV v1.0.0
  - The description on how this model was built can be found [here](https://github.com/theiagen/VADR_models)
  - The exception is that Dengue and other Flaviviridae model files are located at `/opt/vadr/vadr-models-flavi/` within the container filesystem. To use these models, please specify the 2 options: `v-annotate.pl --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi`. A full example command can be found below.

### VADR Documentation

- [Full documentation](https://github.com/ncbi/vadr#vadr-documentation-)
- [Docs on Dengue and other Flaviviridae annotation](https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#dengue-virus-and-other-flaviviridae-refseq-vadr-models)

## Example Usage

```bash
# trim terminal Ns from my input genome (VADR requires this as the first step)
# for MPXV, adjust maxlen to 210000
fasta-trim-terminal-ambigs.pl \
    input.fa \
    --minlen 50 \
    --maxlen 30000 \
    > trimmed.fasta

# run v-annotate.pl using Flaviviridae model to annotate a Dengue viral genome
v-annotate.pl --split --cpu 1 --group Dengue --nomisc --noprotid \
    --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi \
    GCF_000862125.1_ViralProj15306_genomic.fna \
    dengue-test-outdir

# run v-annotate.pl using HAV models to annotate an HAV FASTA file
# the "-mkey hav.vadr" option is required to specify the HAV model
 v-annotate.pl --split \
     -r \
     -xnocomp \
     -mkey hav.vadr \
     hav.trimmed.fasta \
     hav-vadr-test-output
```
