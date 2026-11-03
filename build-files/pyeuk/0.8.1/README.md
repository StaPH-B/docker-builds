# PyEuk container

Main tool: [pyeuk](https://github.com/veg/pyeuk)
  
Code repository: https://github.com/veg/pyeuk

Additional tools:
- none

Basic information on how to use this tool:
- executable: `pyeuk`, `cyclospora-typing`
- help: `-h`, `--help`
- version:
- description: A Tool Suite for Catalogue-Free Multilocus Typing

Additional information:

Pond, S. K., Callan, D., & Nekrutenko, A. (2026). PyEuk: a tool suite for catalogue-free multilocus typing. bioRxiv, 2026.09.10.750732. https://doi.org/10.64898/2026.09.10.750732‌
  
Full documentation: https://github.com/veg/pyeuk

## Example Usage

### Amplicon
```bash
# Optional: derive target panel de novo from coverage peaks if coordinates are unknown
pyeuk derive-panel ref_genome.fasta --bams bams/*.bam -o derived_panel.fasta

# 1. Define cohort-wide analysis windows from read alignments
pyeuk define-windows panel.fasta --bams bams/*.bam -o windows.bed

# 2. Call physically phased microhaplotypes for each specimen
mkdir -p calls
for bam in bams/*.bam; do
    sample=$(basename "$bam" .bam)
    pyeuk call-haplotypes --bam "$bam" --ref panel.fasta --specimen "$sample" \
        --bed windows.bed --out "calls/${sample}.tsv"
done

# 3. Assemble binary specimen-by-haplotype presence/absence matrix
pyeuk build-sheet calls/ output_matrix/

# 4. Calculate pairwise dropout-tolerant weighted IBS distances
pyeuk eukaryotyping -i output_matrix/haplotype_data_sheet.txt \
    -o distance_matrix.csv --wibs

# 5. Run hierarchical clustering with partition stability sweep
pyeuk cluster -m distance_matrix.csv -o clusters_detected/

# 6. Render visual HTML dashboard report
pyeuk report clusters_detected/*_SWEEP.json -o report.html --matrix distance_matrix.csv
```
### Alternative Ingestion Modes
```bash
# Ingest assembled FASTA contigs reference-free de novo
pyeuk run-all \
    -a example_data/cohort_contigs.fasta \
    --de-novo \
    -o ./de_novo_results

# Ingest directory of specimen call files (or .zip)
pyeuk run-all \
    -s example_data/specimens \
    -g example_data/gold_clusters.tsv \
    -o ./cyclospora_outbreak_results

```
