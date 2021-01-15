# SerotypeFinder Container How-To

### Description
Tool for serotyping E. coli isolates from reads or assemblies.

### Version information
SerotypeFinder version: 2.0.1 https://bitbucket.org/genomicepidemiology/serotypefinder/src/2.0.1/

SerotypeFinder database version: Git commit `39c68c6e1a3d94f823143a2e333019bb3f8dddba` made on 2020‑09‑24. [Link to commit history](https://bitbucket.org/genomicepidemiology/serotypefinder_db/commits/)

Web tool: https://cge.cbs.dtu.dk/services/SerotypeFinder/

## Requirements
  * Docker or Singularity
  * E. coli raw reads (fastq.gz) or assembly (fasta)
    * Illumina, Ion Torrent, Roche 454, SOLiD, Oxford Nanopore, and PacBio reads are supported. (I've only tested ILMN reads)

## Notes
  * SerotypeFinder does **NOT** create an output directory when you use the `-o` flag. You MUST create it beforehand.
  * It is recommended to use raw reads, due to the increased sensitivity (without loss of specificity) and the additional information gleaned from KMA output (specifically the depth metric). You also save time from having to assemble the genome first

## Example Usage: Docker
```
pangolin --threads {threads} --outdir {pangolin_results} {fasta}
```

## Example Usage: Singularity
```

```
