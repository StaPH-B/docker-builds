# stxtyper container

Main tool: [stxtyper](https://github.com/ncbi/stxtyper)

Additional tools:

- ncbi-blast+ 2.12.0

Basic information on how to use this tool:

- executable: `stxtyper`
- help: `stxtyper --help`
- version: `stxtyper --version`
- description: Detects and types Shiga toxin genes in nucleotide sequences

Full documentation: [https://github.com/ncbi/stxtyper](https://github.com/ncbi/stxtyper)

Note: [This software is now incorporated into NCBI's AMRFinderPlus software as of version 4.0.3](https://github.com/ncbi/amr/releases/tag/amrfinder_v4.0.3). Stxtyper will run under-the-hood of AMRFinderPlus when using the `amrfinder --organism Escherichia` option.

## Example Usage

```bash
# stxtyper accepts both gzipped and uncompressed FASTA files
stxtyper -n GCA_012224845.2_ASM1222484v2_genomic.fna.gz -o stxtyper-results.tsv

$ column -t test-result.tsv 
#target_contig  stx_type  operon    identity  target_start  target_stop  target_strand  A_reference  A_reference_subtype  A_identity  A_coverage  B_reference  B_reference_subtype  B_identity  B_coverage
CP113091.1      stx2o     COMPLETE  100.00    2085533       2086768      +              WAK52085.1   stxA2o               100.00      100.00      QZL10983.1   stxB2o               100.00      100.00
```
