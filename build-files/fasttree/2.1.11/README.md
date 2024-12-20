Main tool: FastTree v2.1.11
Full documentation: http://www.microbesonline.org/fasttree/

**Docker container information:**

This Docker container installs and runs FastTree using Ubuntu Bionic as a base image. No other dependencies are needed to run FastTree.
The small sequence alignment (covid_alignment.fasta) also in the container is used to test the Docker build.

**Usage for FastTree version 2.1.11**

FastTree infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences. 

FastTree can handle alignments with up to a million of sequences in a reasonable amount of time and memory. 

FastTree accepts alignments in fasta or phylip interleaved formats

```
FastTree protein_alignment > tree

FastTree < protein_alignment > tree

FastTree -out tree protein_alignment

FastTree -nt nucleotide_alignment > tree

FastTree -nt -gtr < nucleotide_alignment > tree

FastTree < nucleotide_alignment > tree
 
Common options (must be before the alignment file):
  
  -quiet to suppress reporting information
  
  -nopr to suppress progress indicator
  
  -log logfile -- save intermediate trees, settings, and model details
  
  -fastest -- speed up the neighbor joining phase & reduce memory usage (recommended for >50,000 sequences)
  
  -n <number> to analyze multiple alignments (phylip format only) (use for global bootstrap, with seqboot and CompareToBootstrap.pl)
  
  -nosupport to not compute support values
 
  -intree newick_file to set the starting tree(s)
  
  -intree1 newick_file to use this starting tree for all the alignments (for faster global bootstrap on huge alignments)
  
  -pseudo to use pseudocounts (recommended for highly gapped sequences)
  
  -gtr -- generalized time-reversible model (nucleotide alignments only)
  
  -lg -- Le-Gascuel 2008 model (amino acid alignments only)
  
  -wag -- Whelan-And-Goldman 2001 model (amino acid alignments only)
  
  -quote -- allow spaces and other restricted characters (but not ' ) in
    sequence names and quote names in the output tree (fasta input only;
    FastTree will not be able to read these trees back in
  
  -noml to turn off maximum-likelihood
  
  -nome to turn off minimum-evolution NNIs and SPRs
    (recommended if running additional ML NNIs with -intree)
  
  -nome -mllen with -intree to optimize branch lengths for a fixed topology
  
  -cat # to specify the number of rate categories of sites (default 20)
  
  -nocat to use constant rates
  
  -gamma -- after optimizing the tree under the CAT approximation, rescale the lengths to optimize the Gamma20 likelihood
  
  -constraints constraintAlignment to constrain the topology search constraintAlignment should have 1s or 0s to indicates splits
  
  -expert -- see more options  
```

**Example command-line input for basic FastTree phylogeny**

```
FastTree -log fasttree_test_log -nt sample.fasta > fasttree_test.nwk
```
  
  For more information, see http://www.microbesonline.org/fasttree/
