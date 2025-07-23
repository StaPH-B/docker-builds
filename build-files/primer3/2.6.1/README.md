# Primer3 container

Main tool: [Primer3](https://github.com/primer3-org/primer3)
  
Code repository: https://github.com/primer3-org/primer3

Basic information on how to use this tool:
- executable: | 
    primer3_core
    ntdpal
    oligotm
    long_seq_tm_test
- help: NA
- version: NA
- description: |

> Design PCR primers from DNA sequence. 

Additional information: 

If thermodynamic parameters are required, configuration files are available inside the container at `/usr/share/primer3_config`.
  
Full documentation: https://primer3.org/manual.html

## Example Usage

### Example Input File
```
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
```bash
primer3_core < input.txt
```
