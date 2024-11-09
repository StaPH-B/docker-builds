# Augur Container

Main tool: [Augur](https://github.com/nextstrain/augur)

Additional tools:

- mafft 7.505
- iqtree2 2.0.7
- raxml 8.2.12
- fasttree 2.1.11
- vcftools 0.1.16
- biopython 1.84
- matplotlib 3.9.2
- numpy 1.26.4
- pandas 1.5.3
- phylo-treetime 0.11.4
- python 3.11.10
- scipy 1.14.1

Definition: One held to foretell events by omens.

Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data. It provides a collection of commands which are designed to be composable into larger processing pipelines.

The output of augur is a series of JSONs that can be used to visualize your results using Auspice.

Note: Auspice is a different tool.

## Example Usage

```bash
augur index --sequences sequences.fasta --output sequence_index.tsv
```

```bash
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
