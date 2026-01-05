# Augur Container

Main tool: [Augur](https://github.com/nextstrain/augur)

Definition: One held to foretell events by omens.

Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data. It provides a collection of commands which are designed to be composable into larger processing pipelines.

The output of augur is a series of JSONs that can be used to visualize your results using Auspice.

Note: Auspice is a different tool.

## Additional dependencies

- fasttree 2.1.11-2
- python 3.11.13
- iqtree 2.0.7+dfsg-1+b2
- mafft 7.505-1
- raxml 8.2.13+dfsg-2+b1
- vcftools 0.1.16-3+b1
- seqkit 2.12.0

<details>

<summary>Additional tools installed via pip:</summary>

```

Package                   Version
------------------------- -----------
attrs                     25.4.0
bcbio-gff                 0.7.1
biopython                 1.86
contourpy                 1.3.3
cvxopt                    1.3.2
cycler                    0.12.1
fonttools                 4.61.1
isal                      1.8.0
isodate                   0.7.2
jsonschema                4.25.1
jsonschema-specifications 2025.9.1
kiwisolver                1.4.9
matplotlib                3.10.8
networkx                  3.6.1
nextstrain-augur          32.1.0
numpy                     2.4.0
packaging                 25.0
pandas                    2.3.3
phylo-treetime            0.11.4
pillow                    12.1.0
pip                       24.0
pyfastx                   2.2.0
pyparsing                 3.3.1
python-calamine           0.6.1
python-dateutil           2.9.0.post0
pytz                      2025.2
PyYAML                    6.0.3
referencing               0.37.0
rpds-py                   0.30.0
scipy                     1.16.3
setuptools                79.0.1
six                       1.17.0
typing_extensions         4.15.0
tzdata                    2025.3
wheel                     0.45.1
xopen                     2.0.2
zlib-ng                   1.0.0
zstandard                 0.25.0

```

</details>

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
  --output-sequences results/filtered.fasta \
  --group-by country year month \
  --sequences-per-group 20 \
  --min-date 2012
```

Better documentation can be found [here.](https://docs.nextstrain.org/en/latest/tutorials/creating-a-workflow.html)
