# toulligQC container

Main tool: [toulligQC](https://github.com/GenomiqueENS/toulligQC)
  
Code repository: https://github.com/GenomiqueENS/toulligQC


Basic information on how to use this tool:
- executable: toulligqc
- help: --help
- version: --version
- description: |
> ToulligQC is dedicated to the QC analyses of Oxford Nanopore runs.
  
Full documentation: https://github.com/GenomiqueENS/toulligQC

## Example Usage

```bash
# Sequencing summary alone
toulligqc --report-name summary_only \
            --sequencing-summary-source /path/to/basecaller/output/sequencing_summary.txt \
            --html-report-path /path/to/output/report.html

# Sequencing summary + telemetry file
toulligqc --report-name summary_plus_telemetry \
            --telemetry-source /path/to/basecaller/output/sequencing_telemetry.js \
            --sequencing-summary-source /path/to/basecaller/output/sequencing_summary.txt \
            --html-report-path /path/to/output/report.html

# Telemetry file + fast5 files
toulligqc --report-name telemetry_plus_fast5 \
            --telemetry-source /path/to/basecaller/output/sequencing_telemetry.js \
            --fast5-source /path/to/basecaller/output/fast5_files.fast5.gz \ 
            --html-report-path /path/to/output/report.html
# Fastq/ bam files only
toulligqc --report-name FAF0256 \
            --fastq /path/to/basecaller/output/fastq_files.fq.gz \ # (replace with --bam)
            --html-report-path /path/to/output/report.html

# Optional arguments for 1D² analysis
toulligqc --report-name FAF0256 \
            --telemetry-source /path/to/basecaller/output/sequencing_telemetry.js \
            --sequencing-summary-source /path/to/basecaller/output/sequencing_summary.txt \
            --sequencing-summary-1dsqr-source /path/to/basecaller/output/sequencing_1dsqr_summary.txt \ # (optional)
            --html-report-path /path/to/output/report.html

# Optional arguments to deal with barcoded samples
toulligqc --report-name FAF0256 \
            --barcoding \
            --telemetry-source /path/to/basecaller/output/sequencing_telemetry.js \
            --sequencing-summary-source /path/to/basecaller/output/sequencing_summary.txt \
            --sequencing-summary-source /path/to/basecaller/output/barcoding_summary_pass.txt \         # (optional)
            --sequencing-summary-source /path/to/basecaller/output/barcoding_summary_fail.txt \         # (optional)
            --sequencing-summary-1dsqr-source /path/to/basecaller/output/sequencing_1dsqr_summary.txt \ # (optional)
            --sequencing-summary-1dsqr-source /path/to/basecaller/output/barcoding_summary_pass.txt \   # (optional)
            --sequencing-summary-1dsqr-source /path/to/basecaller/output/barcoding_summary_fail.txt \   # (optional)
            --html-report-path /path/to/output/report.html \
            --data-report-path /path/to/output/report.data \                                            # (optional)
            --barcodes BC01,BC02,BC03
```
