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
- MPOX/mpxv version 1.4.2-1 (`-mkey mpxv`)

Most of the VADR model files are located at `/opt/vadr/vadr-models` in the container filesystem and this path is stored in the globally accessible bash variable `$VADRMODELDIR`. For most applications, there is no need to specify `v-annotate.pl --mdir /path/to/model/files` since `$VADRMODELDIR` is set in the environment. Flaviviridae model files are located at `/opt/vadr/vadr-models-flavi/` within the container filesystem. To use these models, please specify the 2 options: `v-annotate.pl --mdir /opt/vadr/vadr-models-flavi/ --mkey flavi`.

Be aware that some Mpox sequences may take up to **30 minutes** to annotate, depending on how divergent it is from the RefSeq NC_063383 sequence. Some sequences may only take a minute or so.

Full documentation: https://github.com/ncbi/vadr#vadr-documentation-
Caliciviridae model documentation: https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#norovirus-and-other-caliciviridae-refseq-vadr-models
Flaviviridae model documentation: https://github.com/ncbi/vadr/wiki/Available-VADR-model-files#dengue-virus-and-other-flaviviridae-refseq-vadr-models
MPOX/MPXV model documentation: https://github.com/ncbi/vadr/wiki/Mpox-virus-annotation)

## Example Usage

```bash
# trim terminal Ns from my input genome (VADR requires this as the first step)
# for MPXV, adjust maxlen to 210000
fasta-trim-terminal-ambigs.pl \
    input.consensus.fa \
    --minlen 50 \
    --maxlen 210000 \
    > trimmed.fasta

# run v-annotate.pl using mpxv model
v-annotate.pl --split --cpu 8 --glsearch -s -r --nomisc --mkey mpxv \
    --r_lowsimok --r_lowsimxd 100 --r_lowsimxl 2000 --alt_pass discontn,dupregin \
    --minimap2 --s_overhang 150 \
    trimmed.fasta \
    mpxv-test-output

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
