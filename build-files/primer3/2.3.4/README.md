# Primer3 Container

## Main Tool
**Primer3**  
Repository: [https://github.com/primer3-org/primer3](https://github.com/primer3-org/primer3)  
Documentation: [https://primer3.org/manual.html](https://primer3.org/manual.html)

## Description
> Primer3 designs PCR primers from DNA sequences.

This container provides both the `primer3_core` executable and access to the `primer3_config` directory for thermodynamic calculations if required.

## Executables
- `primer3_core`
- `primer3_config` (for configuration files, not a binary)

## Usage
- Help: `primer3_core --help`
- Version: _Please specify the version if available (e.g., `primer3_core --version`)_

If thermodynamic parameters are required, configuration files are available inside the container (typically found under `/usr/share/primer3_config` or a similar path depending on build).

## Example Input File (`input.txt`)
```text
SEQUENCE_ID=example_1
SEQUENCE_TEMPLATE=AGCTAGCTAGCTACGATCGATCGATCGATCGTACGTAGCTAGCTAGCTGACT
SEQUENCE_TARGET=10,20
PRIMER_TASK=generic
PRIMER_NUM_RETURN=5
PRIMER_MIN_SIZE=18
PRIMER_OPT_SIZE=20
PRIMER_MAX_SIZE=22
PRIMER_MIN_TM=57.0
PRIMER_OPT_TM=60.0
PRIMER_MAX_TM=63.0
PRIMER_MIN_GC=20.0
PRIMER_MAX_GC=80.0
PRIMER_PRODUCT_SIZE_RANGE=100-300
=  
```

### Example Command
```shell
primer3_core < input.txt
```