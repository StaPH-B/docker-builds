# NextPolish2 container

Main tool: [NextPolish2](https://github.com/Nextomics/NextPolish2)
  
Code repository: https://github.com/Nextomics/NextPolish2

Additional tools:
- yak: 0.1-r69
- meryl: 1.4.2
- winnowmap: 2.03
- samtools: 1.24
- minimap2: 2.31-r1302

Basic information on how to use this tool:
- executable: `nextPolish2`
- help: `-h`, `--help `
- version: `-V`, `--version`
- description: Repeat-aware polishing tool for genomes assembled using PacBio HiFi long reads

Additional information:

Jiang Hu, Zhuo Wang, Fan Liang, Shan-Lin Liu, Kai Ye, De-Peng Wang, NextPolish2: A Repeat-aware Polishing Tool for Genomes Assembled Using HiFi Long Reads, Genomics, Proteomics & Bioinformatics, 2024, qzad009, https://doi.org/10.1093/gpbjnl/qzad009
  
Full documentation: https://github.com/Nextomics/NextPolish2

## Example Usage

```bash
nextPolish2 -t 5 hifi.map.sort.bam asm.fa.gz k21.yak k31.yak > asm.np2.fa
```

 