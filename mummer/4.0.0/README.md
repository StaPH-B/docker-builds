# mummer  container
Main tool : [mummer](https://github.com/mummer4/mummer)
# Example Usage

### mummer is a suffix tree algorithm designed to find maximal exact matches of some minimum length between two input sequences.
```{bash}
mummer -mum -b -c H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta > mummer.mums
```
### A dotplot of all the MUMs between two sequences can reveal their macroscopic similarity.

### <span style="color: red"> WARNING!!! </span> Unless running the container interactively; you must use the option --terminal png
```{bash}
mummerplot -x "[0,275287]" -y "[0,265111]" --terminal png -postscript -p mummer mummer.mums
```
### Like mummer, nucmer can handle multiple reference and query sequences, however this example will demonstrate the alignment of multiple query sequences to a single reference.
```{bash}
nucmer -mumreference -c 100 -p nucmer B_anthracis_Mslice.fasta B_anthracis_contigs.fasta
```
### To view a summary of all the alignments produced by NUCmer, we can run the nucmer.delta file through the show-coords utility.
```{bash}
show-coords -r -c -l nucmer.delta > nucmer.coords
```
### promer is a close relative to the NUCmer script. It follows the exact same steps as NUCmer and even uses most of the same programs in its pipeline, with one exception - all matching and alignment routines are performed on the six frame amino acid translation of the DNA input sequence.
```{bash}
promer -p promer_100 -c 100  H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta
```
Better documentation can be found at [https://github.com/mummer4/mummer](https://github.com/mummer4/mummer)

A tutorial can be found at [https://mummer4.github.io/tutorial/tutorial.html](https://mummer4.github.io/tutorial/tutorial.html)

And the manual can be found at [http://mummer.sourceforge.net/manual/](http://mummer.sourceforge.net/manual/)
