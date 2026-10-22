# SeqKit container

Main tool : [SeqKit](https://github.com/shenwei356/seqkit)
  
Code repository: https://github.com/shenwei356/seqkit

Basic information on how to use this tool:
- executable: seqkit
- help: --help 
- version: version
- description: SeqKit is a cross-platform and ultrafast toolkit for FASTA/Q file manipulation.

Full documentation: http://bioinf.shenwei.me/seqkit

## Example Usage

```bash
# get simple statistics from FASTA/Q files

seqkit stats <file name(s)>

# or with flags

seqkit stats --all --tabular <file name(s)>

# conversion from FASTA to FASTQ

seqkit fa2fq <file name(s)>
```
