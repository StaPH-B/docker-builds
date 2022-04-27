# QUAST

This image implements the Genome assembly evaluation tool [QUAST](https://github.com/ablab/quast).
Documentation is available at http://quast.sourceforge.net/docs/manual.html. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (a genome assembly)
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# Run program to QC an assembly
quast.py \
  --output-dir results \
  --min-contig 100 \
  --gene-finding \
  --gene-thresholds 300 \
  --contig-thresholds 500,1000 \
  --strict-NA \
  NCTC13799.fna
```

## Example output

The on-screen output tells you what the program did and what files it generated:
```
Version: 5.0.2

System information:
  OS: Linux-5.10.104-linuxkit-x86_64-with-Ubuntu-16.04-xenial (linux_64)
  Python version: 2.7.12
  CPUs number: 3

Started: 2022-04-27 07:37:42

Logging to /data/results/quast.log
NOTICE: Maximum number of threads is set to 1 (use --threads option to set it manually)

CWD: /data
Main parameters: 
  MODE: default, threads: 1, minimum contig length: 100, minimum alignment length: 65, \
  ambiguity: one, threshold for extensive misassembly size: 1000

Contigs:
  Pre-processing...
  NCTC13799.fna ==> NCTC13799

2022-04-27 07:37:43
Running Basic statistics processor...
  Contig files: 
    NCTC13799
  Calculating N50 and L50...
    NCTC13799, N50 = 2172222, L50 = 1, Total length = 2172222, GC % = 52.56, # N's per 100 kbp =  0.00
  Drawing Nx plot...
    saved to /data/results/basic_stats/Nx_plot.pdf
  Drawing cumulative plot...
    saved to /data/results/basic_stats/cumulative_plot.pdf
  Drawing GC content plot...
    saved to /data/results/basic_stats/GC_content_plot.pdf
  Drawing NCTC13799 GC content plot...
    saved to /data/results/basic_stats/NCTC13799_GC_content_plot.pdf
Done.

2022-04-27 07:37:44
Running GeneMarkS...
  NCTC13799

WARNING: License period for GeneMark has ended! 
To update license, please visit http://exon.gatech.edu/GeneMark/license_download.cgi page and fill in the form.
You should choose GeneMarkS tool and your operating system (note that GeneMark is free for non-commercial use).
Download the license key and replace your ~/.gm_key with the updated version. After that you can restart QUAST.


NOTICE: Genes are not predicted by default. Use --gene-finding or --glimmer option to enable it.

2022-04-27 07:37:44
Creating large visual summaries...
This may take a while: press Ctrl-C to skip this step..
  1 of 2: Creating Icarus viewers...
  2 of 2: Creating PDF with all tables and plots...
Done

2022-04-27 07:37:44
RESULTS:
  Text versions of total report are saved to /data/results/report.txt, report.tsv, and report.tex
  Text versions of transposed total report are saved to /data/results/transposed_report.txt, transposed_report.tsv, and transposed_report.tex
  HTML version (interactive tables and plots) is saved to /data/results/report.html
  PDF version (tables and plots) is saved to /data/results/report.pdf
  Icarus (contig browser) is saved to /data/results/icarus.html
  Log is saved to /data/results/quast.log

Finished: 2022-04-27 07:37:44
Elapsed time: 0:00:02.811139
NOTICEs: 2; WARNINGs: 1; non-fatal ERRORs: 0

Thank you for using QUAST!
```
