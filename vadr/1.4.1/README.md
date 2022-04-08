# VADR container

Main tool : [<program>](https://github.com/ncbi/vadr)

Full documentation for SARS-CoV-2 annotation : https://github.com/ncbi/vadr/wiki/Coronavirus-annotation

> VADR [Viral Annotation DefineR] is a suite of tools for classifying and analyzing sequences homologous to a set of reference models of viral genomes or gene families.

# Example Usage

```
fasta-trim-terminal-ambigs.pl --minlen 50 --maxlen 30000 sequences.fasta > trimmed_sequences.fasta

v-annotate.pl --split \
  --glsearch \
  -s \
  -r \
  --nomisc \
  --lowsim5seq 6 \
  --lowsim3seq 6 \
  --alt_fail lowscore,insertnn,deletinn \
  --cpu 4 \
  --noseqnamemax \
  --mkey sarscov2 \
  --mdir /opt/vadr/vadr-models \
  trimmed_sequences.fasta \
  vadr
```
