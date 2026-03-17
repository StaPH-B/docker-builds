
# artic-tools container

Main tool: [artic-tools](https://github.com/will-rowe/artic-tools)
  
Code repository: https://github.com/will-rowe/artic-tools

Basic information on how to use this tool:
- executable: artic-tools
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: 
> A set of tools for working with the ARTIC pipeline.

Additional Tools:
- ca-certificates
- HTSlib
- Boost
- Curl GnuTLS
- C++17

Additional information and Full Documentation:

* Information about [primer schemes](https://github.com/will-rowe/artic-tools/blob/master/docs/primerscheme.md).
* [Commands](https://github.com/will-rowe/artic-tools/blob/master/docs/commands.md)
    * align_trim: Trim alignments from an amplicon scheme
    * get_scheme: Download an ARTIC primer scheme and reference sequence
    * validate_scheme: Validate an amplicon scheme for compliance with ARTIC standards
    * check_vcf: Check a VCF file based on primer scheme info and user-defined cut offs
* Help output for subcommands:
    * align_trim
    ```
    Trim alignments from an amplicon scheme
    Usage: artic-tools align_trim [OPTIONS] scheme

    Positionals:
    scheme TEXT:FILE REQUIRED The ARTIC primer scheme

    Options:
    -h,--help Print this help message and exit
    -b,--inputFile TEXT The input BAM file (will try STDIN if not provided)
    --minMAPQ UINT A minimum MAPQ threshold for processing alignments (default = 15)
    --normalise UINT Subsample to N coverage per strand (default = 100, deactivate with 0)
    --report TEXT Output an align_trim report to file
    --start Trim to start of primers instead of ends
    --remove-incorrect-pairs Remove amplicons with incorrect primer pairs
    --no-read-groups Do not divide reads into groups in SAM output
    --verbose Output debugging information to STDERR
    ```
    * get_scheme
    ```
    Download an ARTIC primer scheme and reference sequence
    Usage: artic-tools get_scheme [OPTIONS] scheme

    Positionals:
    scheme TEXT REQUIRED The name of the scheme to download (ebola|nipah|scov2)

    Options:
    -h,--help Print this help message and exit
    --schemeVersion UINT=0 The ARTIC primer scheme version (default = latest)
    -o,--outDir TEXT The directory to write the scheme and reference sequence to
    ```
    * validate_scheme
    ```
    Validate an amplicon scheme for compliance with ARTIC standards
    Usage: artic-tools validate_scheme [OPTIONS] scheme

    Positionals:
    scheme TEXT:FILE REQUIRED The primer scheme to validate

    Options:
    -h,--help Print this help message and exit
    -o,--outputPrimerSeqs TEXT If provided, will write primer sequences as multiFASTA (requires --refSeq to be provided)
    -r,--refSeq TEXT The reference sequence for the primer scheme (FASTA format)
    --outputInserts TEXT If provided, will write primer scheme inserts as BED (exluding primer sequences)
    ```
    * check_vcf
    ```
    Check a VCF file based on primer scheme info and user-defined cut offs
    Usage: artic-tools check_vcf [OPTIONS] vcf scheme

    Positionals:
    vcf TEXT:FILE REQUIRED The input VCF file to filter
    scheme TEXT:FILE REQUIRED The primer scheme to use
    
    Options:
    -h,--help Print this help message and exit
    -o,--summaryOut TEXT REQUIRED
    Summary of variant checks will be written here (TSV format)
    --vcfOut TEXT If provided, will write variants that pass checks to this file
    -q,--minQual FLOAT Minimum quality score to keep a variant (default = 10)
    ```
## Example Usage

align_trim
```bash
artic-tools align_trim -b in.bam primerscheme.bed > out.bam 2> out.log
```

get_scheme
```bash
artic-tools artic-tools get_scheme nipah
```

validate_scheme
```bash
artic-tools artic-tools validate_scheme primerscheme.bed
```

check_vcf
```bash
artic-tools check_vcf -o summary.txt --vcfOut variants_passed.txt CVR1.merged.vcf.gz SCoV2.scheme.v3.bed
```