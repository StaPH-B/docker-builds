# mummer + RGDv2 container

Main tool : [mummer](https://github.com/mummer4/mummer)

Additional tools:

- fig2dev (3.2.3)
- gnuplot (4.0)
- xfig (3.2)

MUMmer is a versatile alignment tool for DNA and protein sequences.


Better documentation for Mummer can be found at [https://github.com/mummer4/mummer](https://github.com/mummer4/mummer)

A tutorial can be found at [https://mummer4.github.io/tutorial/tutorial.html](https://mummer4.github.io/tutorial/tutorial.html)

And the manual can be found at [http://mummer.sourceforge.net/manual/](http://mummer.sourceforge.net/manual/)

## Example Usage
```bash
mummer -mum -b -c H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta > mummer.mums
mummerplot -x "[0,275287]" -y "[0,265111]" --terminal png -postscript -p mummer mummer.mums
nucmer  -c 100 -p nucmer B_anthracis_Mslice.fasta B_anthracis_contigs.fasta
show-snps -C nucmer.delta > nucmer.snp
promer -p promer_100 -c 100  H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta
mummerplot -l nucmer.delta -p test_mummer_plot --png
gnuplot test_mummer_plot.gp
```