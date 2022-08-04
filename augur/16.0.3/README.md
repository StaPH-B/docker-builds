# Augur Container
Main tool: [Augur](https://github.com/nextstrain/augur)

Definition: One held to foretell events by omens.

Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data. It provides a collection of commands which are designed to be composable into larger processing pipelines.

The output of augur is a series of JSONs that can be used to visualize your results using Auspice.

# Example Usage

```
augur index --sequences sequences.fasta --output sequence_index.tsv
```

```
augur filter \
  --sequences data/sequences.fasta \
  --sequence-index results/sequence_index.tsv \
  --metadata data/metadata.tsv \
  --exclude config/dropped_strains.txt \
  --output results/filtered.fasta \
  --group-by country year month \
  --sequences-per-group 20 \
  --min-date 2012
```

Better documentation can be found [here.](https://docs.nextstrain.org/en/latest/tutorials/creating-a-workflow.html)
