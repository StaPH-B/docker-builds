# masurca container

Main tools:
- [masurca](https://github.com/alekseyzimin/masurca)
- [polca](https://github.com/alekseyzimin/masurca#polca)
- [Chromosome scaffolder](https://github.com/alekseyzimin/masurca#chromosome-scaffolder)
- [SAMBA](https://github.com/alekseyzimin/masurca#samba-scaffolder)

Other tools:
- [bwa](http://bio-bwa.sourceforge.net/) (used by polca)
- [minimap2](https://github.com/lh3/minimap2) (used by samba)

# Example Usage

```
# polishes consensus genome with paired-end Illumina reads
polca.sh -a genome.fasta -r 'reads1.fastq reads2.fastq.gz' -t 16 -m 1G
```

Better documentation can be found at [https://github.com/alekseyzimin/masurca](https://github.com/alekseyzimin/masurca)
