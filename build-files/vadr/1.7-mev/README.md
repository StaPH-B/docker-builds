# VADR container

Main tool : [VADR](https://github.com/NLM-DIR/vadr)

Additional tools:

- perl v5.34.0
- infernal v1.1.5
- ncbi-blast+ v2.15.0
- fasta v36.3.8h (the tool, not the file format)
- minimap2 2.26-r1175

Basic information on how to use this tool:

- executable: `v-annotate.pl`
- additional executable: `fasta-trim-terminal-ambigs.pl`
- help: `-h`
- version: `-v`

## Description

> VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

## Additional information

Included models:

- MeV/Measles version 1.02 (`-mkey mev`)

Most of the VADR model files are located at `/opt/vadr/vadr-models` in the container filesystem and this path is stored in the globally accessible bash variable `$VADRMODELDIR`. For most applications, there is no need to specify `v-annotate.pl --mdir /path/to/model/files` since `$VADRMODELDIR` is set in the environment.

- Full documentation: https://github.com/NLM-DIR/vadr/wiki
- MeV documentation: https://github.com/greninger-lab/vadr-models-mev

Please note that VADR may need a large amount of RAM (>16 GB) for many MeV sequences, especially those that are highly divergent.

:warning: **This docker image DOES contain other VADR models by default.** We originally intended for this to only contain the Measles VADR model files, but a change in v1.7's installation script resulted in the models being included in the image. We have left the models in the image for now and have created a separate docker image `staphb/vadr:1.7-slim` which does not include the models. Please see the dockerfile & README here for the actual "slim" version of the vadr docker image: [`build-files/vadr/1.7-slim/`](./1.7-slim/).

These model files are included:

- Coronaviridae (coronaviruses including sars-cov-2) v1.3-3
- Influenza v1.6.3-2
- MPXV v1.4.2-1
- RSV v1.5-2
- SARS-CoV-2 v1.3-2

## Example Usage

```bash
# trim fasta file
fasta-trim-terminal-ambigs.pl input.consensus.fa > trimmed.fasta

# run v-annotate.pl using RSV models
v-annotate.pl --split 
  -r \
  -xnocomp \
  -mkey mev \
  trimmed.fasta \
  mev-test-output
```

