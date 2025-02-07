# Core-SNP-filter container

Main tool: [Core-SNP-filter](https://github.com/rrwick/Core-SNP-filter)
  
Code repository: https://github.com/rrwick/Core-SNP-filter

Basic information on how to use this tool:
- executable: coresnpfilter
- help: -h
- version: -V
- description: |

> This is a tool to filter sites (i.e. columns) in a FASTA-format whole-genome pseudo-alignment based on:
> - Whether the site contains variation or not.
> - How conserved the site is, i.e. contains an unambiguous base in a sufficient fraction of the sequences.
  
Full documentation: https://github.com/rrwick/Core-SNP-filter

## Example Usage

```bash
# Exclude invariant sites:
coresnpfilter -e core.full.aln > filtered.aln

# With a strict core threshold (same as Snippy's core.aln):
coresnpfilter -e -c 1.0 core.full.aln > filtered.aln

# With a slightly more relaxed core threshold:
coresnpfilter -e -c 0.95 core.full.aln > filtered.aln

# Use gzipped files to save disk space:
coresnpfilter -e -c 0.95 core.full.aln.gz | gzip > filtered.aln.gz

# Running without any options will work, but the output will be the same as the input:
coresnpfilter core.full.aln > filtered.aln
```
