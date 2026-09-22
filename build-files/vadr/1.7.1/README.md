# VADR container

Main tool : [VADR](https://github.com/NLM-DIR/vadr)

Additional tools:

- fasta v36.3.8h (the tool, not the file format)
- infernal v1.1.5
- minimap2 2.30-r1287
- ncbi-blast+ v2.17.0
- perl v5.34.0
- python3 3.12.3
- R2DT v2.3

Basic information on how to use this tool:

- executable: `v-annotate.pl`
- additional executable: `fasta-trim-terminal-ambigs.pl`
- help: `-h`
- version: `-v`

## Description

> VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

## Additional information

:warning: **This docker image DOES contain VADR models that are downloaded by default with VADR's installation script `vadr-install.sh`.** We originally intended for this to the the slim docker image, but a change in v1.7's installation script resulted in the models being included in the image. We have left the models in the image for now and have created a separate docker image `staphb/vadr:1.7.1-slim` which does not include the models. Please see the dockerfile & README here for the actual "slim" version of the vadr docker image: [`build-files/vadr/1.7.1-slim/`](../1.7.1-slim/).

These model files are included:

- Caliciviridae 1.7-2
- Coronaviridae (coronaviruses including sars-cov-2) v1.3-3
- Flaviviridae 1.7.2 (includes Dengue and HCV)
- Influenza v1.7-2
- MPXV v1.4.2-1
- RSV v1.7-2
- SARS-CoV-2 v1.6.3-1
- Zika 1.7.1-2

The default location for VADR models (bash variable `$VADRMODELDIR`) is `/opt/vadr/vadr-models/`. Some model files are stored in their own subdirectories:
```bash
$ ls -d /opt/vadr/vadr-models*
/opt/vadr/vadr-models         /opt/vadr/vadr-models-flavi  /opt/vadr/vadr-models-mpxv  /opt/vadr/vadr-models-sarscov2
/opt/vadr/vadr-models-corona  /opt/vadr/vadr-models-flu    /opt/vadr/vadr-models-rsv   /opt/vadr/vadr-models-zika
```

A larger list of vadr models can be found in [VADR's documentation](https://github.com/NLM-DIR/vadr/wiki/Available-VADR-model-files) for download and mounting/binding during runtime. An example for SARS-CoV-2 is below.

## Example Usage

```bash
# trim fasta file
fasta-trim-terminal-ambigs.pl input.consensus.fa > trimmed.fasta

# run v-annotate.pl using Flaviviridae model to annotate a Dengue viral genome
v-annotate.pl --split --cpu 1 --group Dengue --nomisc --noprotid \
    --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi \
    trimmed.fasta \
    dengue-test-outdir

# run v-annotate.pl using Caliciviridae model to annotate a Norovirus viral genome
v-annotate.pl \
    trimmed.fasta \
    noro-test-outdir
```

### Downloading a model

```bash
# this image doesn't contain any external models
# this examples downloads the SARS-CoV-2 model
wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/1.3-2/vadr-models-sarscov2-1.3-2.tar.gz
tar -xf vadr-models-sarscov2-1.3-2.tar.gz

# then mount this directory to VADRMODELDIR when running
# example with docker
docker run <user docker flags> -v vadr-models-sarscov2-1.3-2:/opt/vadr/vadr-models staphb/vadr:latest <vadr command>
```
