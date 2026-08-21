# ART container

Main tool: [ART](https://www.niehs.nih.gov/research/resources/software/biostatistics/art)
  
Code repository: https://www.niehs.nih.gov/research/resources/software/biostatistics/art


Basic information on how to use this tool:
- executable: `art_illumina`
- help: 
- version: 
- description: ART is a set of simulation tools to generate synthetic next-generation sequencing reads
 
Full documentation: https://www.niehs.nih.gov/research/resources/software/biostatistics/art

## Example Usage

```bash
# simulation of 30X HiSeq paired-end reads. 150bp with the mean fragment size 500 and standard deviation 10

art_illumina -ss HSxN -i genome.fasta -p -l 150 -f 30 -p -m 500 -s 10 -o prefix_R
```

  
