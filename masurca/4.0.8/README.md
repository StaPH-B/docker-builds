# masurca container

Main tools:
- [masurca](https://github.com/alekseyzimin/masurca)
- [polca](https://github.com/alekseyzimin/masurca#polca)
- [Chromosome scaffolder](https://github.com/alekseyzimin/masurca#chromosome-scaffolder)
- [SAMBA](https://github.com/alekseyzimin/masurca#samba-scaffolder)

Additional tools:
- [bwa](http://bio-bwa.sourceforge.net/) (used by polca)
- [minimap2](https://github.com/lh3/minimap2) (used by samba)

Full documentation: https://github.com/alekseyzimin/masurca

> The MaSuRCA (Maryland Super Read Cabog Assembler) genome assembly and analysis toolkit contains of MaSuRCA genome assembler, QuORUM error corrector for Illumina data, POLCA genome polishing software, Chromosome scaffolder, jellyfish mer counter, and MUMmer aligner. 

# Example Usage

```
# polishes consensus genome with paired-end Illumina reads
polca.sh -a genome.fasta -r 'reads1.fastq reads2.fastq.gz' -t 16 -m 1G
```
