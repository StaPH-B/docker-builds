# igv-reports container

Main tool: [igv-reports](https://github.com/igvteam/igv-reports)
  
Code repository: https://github.com/igvteam/igv-reports

Basic information on how to use this tool:
- executable: create_report
- help: -h
- version: NA
- description: Creates igv-style html report of variants

Additional information: |
> A Python application to generate self-contained HTML reports for variant review and other genomic applications. Reports consist of a table of genomic sites and an embedded IGV genome browser for viewing data for each site. The tool extracts slices of data for each site and embeds the data as blobs in the HTML report file. The report can be opened in a web browser as a static page, with no depenency on the original input files.


Full documentation: https://github.com/igvteam/igv-reports

## Example Usage

```bash
create_report input.vcf.gz \
    --fasta reference.fa \
    --flanking 1000 \
    --info-columns GENE TISSUE TUMOR COSMIC_ID GENE SOMATIC \
    --samples reads_1_fastq \
    --sample-columns DP GQ \
    --tracks input.vcf.gz recalibrated.bam \
    --output output.html
```
