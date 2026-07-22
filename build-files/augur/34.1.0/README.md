# Augur Container

Main tool: [Augur](https://github.com/nextstrain/augur)

Definition: One held to foretell events by omens.

Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data. It provides a collection of commands which are designed to be composable into larger processing pipelines.

The output of augur is a series of JSONs that can be used to visualize your results using Auspice.

Note: Auspice is a different tool.

## Additional dependencies

- fasttree 2.1.11-2
- python 3.12.13
- iqtree 2.0.7+dfsg-1+b2
- mafft 7.505-1
- raxml 8.2.13+dfsg-2+b1
- vcftools 0.1.16-3+b1
- seqkit 2.13.0

<details>

<summary>Additional tools installed via pip:</summary>

```
	Package                   Version
	------------------------- -----------
	attrs                     26.1.0
	backports.zstd            1.6.0
	bcbio-gff                 0.7.1
	biopython                 1.87
	contourpy                 1.3.3
	cvxopt                    1.3.3
	cycler                    0.12.1
	docutils                  0.23
	fonttools                 4.63.0
	isal                      1.8.0
	isodate                   0.7.2
	jsonschema                4.26.0
	jsonschema-specifications 2025.9.1
	kiwisolver                1.5.0
	matplotlib                3.11.0
	networkx                  3.6.1
	nextstrain-augur          33.4.1
	numpy                     2.5.0
	packaging                 26.2
	pandas                    2.3.3
	phylo-treetime            0.12.1
	pillow                    12.2.0
	pip                       25.0.1
	pyfastx                   2.3.1
	pyparsing                 3.3.2
	python-calamine           0.7.0
	python-dateutil           2.9.0.post0
	pytz                      2026.2
	PyYAML                    6.0.3
	referencing               0.37.0
	rpds-py                   2026.5.1
	scipy                     1.18.0
	six                       1.17.0
	typing_extensions         4.15.0
	tzdata                    2026.2
	xopen                     2.1.0
	zlib-ng                   1.0.0

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
