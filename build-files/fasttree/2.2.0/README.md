# Main tool: FastTree

Full documentation: http://www.microbesonline.org/fasttree/

## Usage

FastTree infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences. 

FastTree can handle alignments with up to a million of sequences in a reasonable amount of time and memory. 

FastTree accepts alignments in fasta or phylip interleaved formats

```bash
FastTree protein_alignment > tree

FastTree < protein_alignment > tree

FastTree -out tree protein_alignment

FastTree -nt nucleotide_alignment > tree

FastTree -nt -gtr < nucleotide_alignment > tree

FastTree < nucleotide_alignment > tree
```

Example command-line input for basic FastTree phylogeny

```bash
FastTree -log fasttree_test_log -nt sample.fasta > fasttree_test.nwk
```
  
For more information, see http://www.microbesonline.org/fasttree/
