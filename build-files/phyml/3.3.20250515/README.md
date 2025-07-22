# Phyml Container

Main Tool: [Phyml](https://github.com/stephaneguindon/phyml)

Code repository: https://github.com/stephaneguindon/phyml

Paper: http://www.atgc-montpellier.fr/download/papers/phyml_2010.pdf

Full documentation: http://www.atgc-montpellier.fr/phyml/versions.php

> PhyML is a software package that uses modern statistical approaches to analyse alignments of nucleotide or amino acid sequences in a phylogenetic framework. The main tool in this package builds phylogenies under the maximum likelihood criterion. It implements a large number of substitution models coupled to efficient options to search the space of phylogenetic tree topologies.

## Example Usage

```
phyml -i snvAlignment.phy --datatype nt --model GTR -v 0.0 -s BEST --ts/tv e --nclasses 4 --alpha e --bootstrap -4 --quiet
```
