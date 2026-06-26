# LisSero container

Main tool: [LisSero](https://github.com/MDU-PHL/LisSero)

Code repository: https://github.com/MDU-PHL/LisSero

Additional tools:
- ncbi-blast+ (blastn): >=2.10.0

Basic information on how to use this tool:
- executable: lissero
- help: --help
- version: --version
- description: In silico serogroup prediction for Listeria monocytogenes from assembled genomes

Additional information:

LisSero infers the Listeria monocytogenes serogroup from an assembly by detecting the presence or absence of five markers with BLAST, following the Doumith et al. 2004 multiplex-PCR scheme (Differentiation of the major Listeria monocytogenes serovars by multiplex PCR. J Clin Microbiol 42(8):3819-22). The marker database is bundled with the tool, so no external download is required.

Marker-to-serogroup logic (column order matches the output table):

| Serogroup | prs | lmo0737 | lmo1118 | ORF2110 | ORF2819 |
|-----------|-----|---------|---------|---------|---------|
| 1/2a, 3a    | + | + | - | - | - |
| 1/2b, 3b, 7 | + | - | - | - | + |
| 1/2c, 3c    | + | + | + | - | - |
| 4b, 4d, 4e  | + | - | - | + | + |

A match below the default identity or coverage threshold (95% each) is reported as PARTIAL and treated as absent. An assembly with only prs detected is reported as Nontypable, which can indicate serotype 4a or 4c.

Known behavior: the reference strain EGD-e (GCF_000196035.1, serotype 1/2a) types as 1/2c, 3c in silico. The lmo#### markers are named after EGD-e's own locus tags, so the lmo1118 marker matches EGD-e at full length and the 1/2c logic fires. This reflects the molecular scheme, not a LisSero error. Use a serotype 4b reference such as F2365 (GCF_000008285.1) as a clean control; it types as 4b, 4d, 4e.

Full documentation: https://github.com/MDU-PHL/LisSero

## Example Usage

```bash
# serogroup one or more assemblies; results print as a tab-delimited table
lissero assembly1.fasta assembly2.fasta > lissero.tsv

# adjust the identity and coverage thresholds (defaults are 95)
lissero --min_id 95 --min_cov 95 assembly.fasta
```
