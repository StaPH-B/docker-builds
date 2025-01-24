# panqc container

Main tool: [panqc](https://github.com/maxgmarin/panqc)
  
Code repository: https://github.com/maxgmarin/panqc

Basic information on how to use this tool:
- executable: panqc nrc || panqc utils
- help: --help
- version: NA
- description: |

> The panqc Nucleotide Redundancy Correction (NRC) pipeline adjusts for redundancy at the DNA level within pan-genome estimates in two steps. In step one, all genes predicted to be absent at the Amino Acid (AA) level are compared to their corresponding assembly at the nucleotide level. In cases where the nucleotide sequence is found with high coverage and sequence identity (Query Coverage & Sequence Identity > 90%), the gene is marked as “present at the DNA level”. Next, all genes are clustered and merged using a k-mer based metric of nucleotide similarity. Cases where two or more genes are divergent at the AA level but highly similar at the nucleotide level will be merged into a single “nucleotide similarity gene cluster”. After applying this method the pan-genome gene presence matrix is readjusted according to these results.

  
Full documentation: [https://github.com/maxgmarin/panqc](https://github.com/maxgmarin/panqc)

## Example Usage

```bash
panqc nrc --asms InputAsmPaths.tsv --pg-ref pan_genome_reference.fa --is-rtab gene_presence_absence.Rtab --results_dir results/
```
