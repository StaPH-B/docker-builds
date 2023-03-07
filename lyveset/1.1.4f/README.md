# LYVE version of the Snp Extraction Tool (SET), a method of using hqSNPs to create a phylogeny.

Main tool: [Lyve-SET](https://github.com/lskatz/Lyve-SET)

Additional tools:

- ncbi-blast+ 2.2.31
- python 2.7.12
- python 3.5.2
- bioperl 1.6.924
- cpanminus 1.7040
- NCBI E-utilities
- Git 2.7.4
- VCFTools 0.1.12b
- SAMTools 1.2
- VarScan 2.3.7
- BCFTools 1.3.1
- SMALT 0.7.6
- SNAP 1.0beta.18
- RAxML 8.1.16
- Quake 0.3.5

## Example Usage

### Help:
 	To see the help for any script, run it without options or with --help. For example, set_test.pl -h. The following is the help for the main script, launch_set.pl

### Analyze test data:
	set_test.pl --numcpus 8 lambda lambda

### Analyze your data: 

	set_manage.pl --create yourProject
	# paired end reads have to be shuffled into one file per sample
	shuffleSplitReads.pl --numcpus 8 -o interleaved *.fastq.gz
	# then moved into your project dir
	mv interleaved/*.fastq.gz yourProject/reads/
	# cleanup
	rmdir interleaved
	cp reference.fasta yourProject/ref/
	launch_set.pl --numcpus 8 -ref yourProject/ref/reference.fasta yourProject