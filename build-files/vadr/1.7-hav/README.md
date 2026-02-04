# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)

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

- HAV version 1.0.0 (`-mkey hav.vadr`)

Most of the VADR model files are located at `/opt/vadr/vadr-models` in the container filesystem and this path is stored in the globally accessible bash variable `$VADRMODELDIR`. For most applications, there is no need to specify `v-annotate.pl --mdir /path/to/model/files` since `$VADRMODELDIR` is set in the environment. 

- Full documentation: https://github.com/ncbi/vadr/wiki
- HAV model documentation: https://github.com/theiagen/VADR_models

## Example Usage

```bash
# trim fasta file
fasta-trim-terminal-ambigs.pl input.consensus.fa > trimmed.fasta

# run v-annotate.pl using HAV models to annotate an HAV FASTA file
# the "-mkey hav.vadr" option is required to specify the HAV model
v-annotate.pl --split \
     -r \
     -xnocomp \
     -mkey hav.vadr \
     trimmed.fasta \
     hav-test-output

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
