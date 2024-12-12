# skani container

Main tool : [skani](https://github.com/bluenote-1577/skani)

Full documentation: https://github.com/bluenote-1577/skani/wiki

skani is a program for calculating average nucleotide identity (ANI) from DNA sequences (contigs/MAGs/genomes) for ANI > ~80%.

## Example Usage

Quick ANI calculation:
```bash
skani dist genome1.fa genome2.fa
```
Memory-efficient database search:
```bash
skani sketch genomes/* -o database
skani search -d database query1.fa query2.fa ...
```
All-to-all comparison:
```bash
skani triangle genomes/*
```
