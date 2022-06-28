# Nullarbor Container

Main tool : [Nullarbor](https://github.com/tseemann/nullarbor#readme)

Full documentation: https://github.com/tseemann/nullarbor#readme

Nullarbor is a pipeline to generate complete public health microbiology reports from sequenced isolates.

Original tool developed by Torsten Seeman.

## Example Usage

```bash
nullarbor.pl --name "Run_Name" --ref ./path/to/reference/genome/ref.fasta --input ./path/to/tsv/of/fasq/file/paths/fastq_file_paths.tsv --outdir ./path/to/target/outdir/nullarbor_outdir/ --treebuilder iqtree_slow --taxoner kraken2 --mode all --run
```
