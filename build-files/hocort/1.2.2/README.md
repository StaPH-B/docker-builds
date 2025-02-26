# HoCoRT

Main tool: [HoCoRT v1.2.2](https://github.com/ignasrum/hocort)
Dependencies:  
[bwa-mem2 v2.2.1](https://github.com/bwa-mem2/bwa-mem2)
[histat2 v2.2.1](https://github.com/DaehwanKimLab/hisat2)
[sparsehash v2.0.4](https://github.com/sparsehash/sparsehash)
[sdsl-lite v2.1.1](https://github.com/simongog/sdsl-lite)
[btl_bloomfilter v1.2.1](https://github.com/bcgsc/btl_bloomfilter)
[biobloom v2.3.5](https://github.com/bcgsc/biobloom)
  
Code repository: https://github.com/ignasrum/hocort

Basic information on how to use this tool:
- executable: |
```
hocort --help
usage: hocort [subcommand] [options]

hocort: remove specific organisms from sequencing reads

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  flag: print version

available subcommands:
  subcommand
    map          map reads to a reference genome and output mapped/unmapped reads
    index        build index/-es for supported tools
```

- help: `hocort --help`
- version: `hocort --version`
- description: | 
> Remove specific organisms from sequencing reads. 

  
Full documentation: https://github.com/ignasrum/hocort/wiki


# Testing HoCoRT analysis
```
curl -L -o test/genome.fna https://raw.githubusercontent.com/ignasrum/hocort/main/tests/test_data/fasta/genome.fna

hocort index \
  bowtie2 \
  --input test/genome.fna \
  --output test/hocort_test
```