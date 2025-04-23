# Lima container with Rscripts

Main tool: [lima](https://lima.how/)
  
Code repository: https://github.com/PacificBiosciences/barcoding

Additional tools:
- report_detail.R
- report_summary.R

Basic information on how to use this tool:
- executables: lima, lima-undo
- help: -h
- version: --version
- description: lima is the standard tool to identify barcode and primer sequences in PacBio single-molecule sequencing data.

Additional information:

This container includes two Rscripts that can visualize various metrics from the lima report.
  
Full documentation: https://lima.how/

## Example Usage
```bash
lima [options] <INPUT.bam|xml|fa|fq|gz> <BARCODES.fa> <OUTPUT.bam|xml|fa|fq|gz>

report_summry.R lima.report

report_detail.R lima.report [pdf|png] [barcode_pair_names]
```

