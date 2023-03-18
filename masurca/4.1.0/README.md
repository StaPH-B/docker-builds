# masurca container

Main tools:

- [masurca](https://github.com/alekseyzimin/masurca) 4.1.0
- [polca](https://github.com/alekseyzimin/masurca#polca)
- [Chromosome scaffolder](https://github.com/alekseyzimin/masurca#chromosome-scaffolder)
- [SAMBA](https://github.com/alekseyzimin/masurca#samba-scaffolder)

Other tools:

- [bwa](https://github.com/lh3/bwa) (used by polca) 0.7.17-r1188
- [minimap2](https://github.com/lh3/minimap2) (used by samba) 2.24-r1122

## Example Usage

```bash
# polishes consensus genome with paired-end Illumina reads
polca.sh -a genome.fasta -r 'reads1.fastq reads2.fastq.gz' -t 16 -m 1G
```

Better documentation can be found at [https://github.com/alekseyzimin/masurca](https://github.com/alekseyzimin/masurca)
