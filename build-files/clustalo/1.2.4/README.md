# ClustalO container

Main tool:

* [http://www.clustal.org/omega/](http://www.clustal.org/omega/)

Clustal Omega is used for creating multiple sequence alignments (MSA). It can handle a number of input combinations, including un-aligned unput sequence files, reference alignments, and hidden markov models. See the full description here: [http://www.clustal.org/omega/README](http://www.clustal.org/omega/README).

## Example Usage

```bash
clustalo --in seqs -o output

clustalo --in seqs --profile1 reference-alignment -o output
```