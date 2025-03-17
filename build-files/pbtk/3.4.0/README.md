# pbtk container

Main tool: [pbtk](https://github.com/PacificBiosciences/pbtk)
  
Code repository: https://github.com/PacificBiosciences/pbtk

Basic information on how to use this tool:
- executables:
    - bam2fasta
    - bam2fastq
    - ccs-kinetics-bystrandify
    - extracthifi
    - pbindex
    - pbindexdump
    - pbmerge
    - zmwfilter
- help: -h, --help
- version: --version
- description: PacBio BAM toolkit

Full documentation: https://github.com/PacificBiosciences/pbtk

## Example Usage

```bash
# bam2fasta
bam2fasta -o out in.bam
# bam2fastq
bam2fastq -o out in_1.bam in_2.bam in_3.xml in_4.bam
# ccs-kinetics-bystrandify
ccs-kinetics-bystrandify in.bam out.bam
# extracthifi
extracthifi in.bam out.bam
# pbindex
pbindex in.bam
# pbindexdump
pbindexdump in.bam.pbi > out.json
# pbmerge
pbmerge in1.bam in2.bam in3.bam > out.bam
# zmwfilter
zmwfilter --include 1,2,4,8,16 in.bam out.bam
```
