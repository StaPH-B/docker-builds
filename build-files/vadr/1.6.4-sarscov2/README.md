# VADR container

Main tool : [VADR](https://github.com/ncbi/vadr)
  
Code repository: https://github.com/ncbi/vadr

Additional tools:
- perl v5.34.0
- infernal v1.1.5
- ncbi-blast+ v2.15.0
- fasta v36.3.8h (the tool, not the file format)
- minimap2 2.26-r1175

Basic information on how to use this tool:
- executable: v-annotate.pl
- additional executable: fasta-trim-terminal-ambigs.pl
- help: -h
- version: -v
- description: |

> VADR is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families. It has been mainly tested for analysis of Norovirus, Dengue, and SARS-CoV-2 virus sequences in preparation for submission to the GenBank database.

Additional information: |

Included models
- Caliciviridae version 1.2.1 (including Norovirus virus; default values)
- Flaviviridae version 1.2.1 (including Dengue virus; `--mdir /opt/vadr/vadr-models-flavi/ --mkey flavi`)
- SARS-CoV-2 version 1.3.2 (`--mkey sarscov2`)

Most of the VADR model files are located at `/opt/vadr/vadr-models` in the container filesystem and this path is stored in the globally accessible bash variable `$VADRMODELDIR`. For most applications, there is no need to specify `v-annotate.pl --mdir /path/to/model/files` since `$VADRMODELDIR` is set in the environment. Flaviviridae model files are located at `/opt/vadr/vadr-models-flavi/` within the container filesystem. To use these models, please specify the 2 options: `v-annotate.pl --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi`.

Full documentation: https://github.com/ncbi/vadr#vadr-documentation-
Caliciviridae model documentation: https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#norovirus-and-other-caliciviridae-refseq-vadr-models
Flaviviridae model documentation: https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#dengue-virus-and-other-flaviviridae-refseq-vadr-models
SARS-CoV-2 model documentation: https://github.com/ncbi/vadr/wiki/Coronavirus-annotation

## Example Usage

```bash
# trim fasta file
fasta-trim-terminal-ambigs.pl input.consensus.fa > trimmed.fasta

# run v-annotate.pl using the sarscov2 model to annotate a trimmed input genome
v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
    --mkey sarscov2 --lowsim5seq 6 \
    --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
    trimmed.fasta \
    sarscov2-test-outdir

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
