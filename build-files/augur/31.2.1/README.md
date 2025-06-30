# Augur Container

Main tool: [Augur](https://github.com/nextstrain/augur)

Definition: One held to foretell events by omens.

Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data. It provides a collection of commands which are designed to be composable into larger processing pipelines.

The output of augur is a series of JSONs that can be used to visualize your results using Auspice.

Note: Auspice is a different tool.

## Additional dependencies

- fasttree 2.1.11
- python 3.11.13
- iqtree2 2.0.7
- mafft 7.505
- raxml 8.2.12
- vcftools 0.1.16
- seqkit 2.10.0

<details><summary>Click To see all Packages installed via pip</summary>
```
Package                   Version
------------------------- -----------
attrs                     25.3.0
bcbio-gff                 0.7.1
biopython                 1.85
contourpy                 1.3.2
cvxopt                    1.3.2
cycler                    0.12.1
fonttools                 4.58.4
isal                      1.7.2
isodate                   0.6.1
jsonschema                4.24.0
jsonschema-specifications 2025.4.1
kiwisolver                1.4.8
matplotlib                3.10.3
networkx                  3.5
nextstrain-augur          31.2.1
numpy                     1.26.4
packaging                 25.0
pandas                    2.3.0
phylo-treetime            0.11.4
pillow                    11.2.1
pip                       24.0
pyfastx                   2.2.0
pyparsing                 3.2.3
python-calamine           0.3.2
python-dateutil           2.9.0.post0
pytz                      2025.2
referencing               0.36.2
rpds-py                   0.25.1
scipy                     1.16.0
setuptools                65.5.1
six                       1.17.0
typing_extensions         4.14.0
tzdata                    2025.2
wheel                     0.45.1
xopen                     2.0.2
zlib-ng                   0.5.1
zstandard                 0.23.0
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
  --output results/filtered.fasta \
  --group-by country year month \
  --sequences-per-group 20 \
  --min-date 2012
```

Better documentation can be found [here.](https://docs.nextstrain.org/en/latest/tutorials/creating-a-workflow.html)
