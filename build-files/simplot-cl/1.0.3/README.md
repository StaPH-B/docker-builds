# simplot-cl container

Main tool: [simplot-cl](https://github.com/hodcroftlab/simplot-cl)
  
Code repository: https://github.com/hodcroftlab/simplot-cl

Basic information on how to use this tool:
- executable: simplot.py
- help: `-h`
- description: A Command-Line Similarity Plot Generator

<details>
<summary>Versions as listed in pip freeze:</summary>

```
argcomplete==3.6.3
biopython==1.86   
contourpy==1.3.3  
cycler==0.12.1    
fonttools==4.62.1 
kiwisolver==1.5.0 
matplotlib==3.10.8
numpy==2.4.3      
packaging==26.0   
pandas==3.0.1     
pillow==12.1.1
pyparsing==3.3.2
python-dateutil==2.9.0.post0
six==1.17.0
```

</details>


### Additional information:

A non-GUI extension of SimPlot program by [Lole et al.](https://pubmed.ncbi.nlm.nih.gov/9847317/), this program takes viral genome sequences in FASTA format and does the following:
1. Aligns the sequences (optional, skipped with --no-align)
2. Splits the alignment into overlapping windows of a chosen size.
3. Calculates the pairwise similarity between a query and other sequences in a window.
Note that similarity is calculated for each sliding window as described below:
    - Count how many positions differ between the query and a reference sequence (Hamming distance).
    - Divide that by the number of valid positions (ignoring gaps and Ns depending on your settings).
    - That gives the p-distance: p = differences / valid positions.
    - Then similarity = 1 − p . That’s what’s plotted along the genome.
4. Produces the following:
    1. A plot showing how similarity changes along the genome
        - Genome position on the x-axis.
        - Similarity (1 - p-distance) on the y-axis.
        - One line per reference sequence (colored by genotype if available).
    2. A CSV table with similarity values (optional).
  
Full documentation: https://github.com/hodcroftlab/simplot-cl/blob/main/README.md

### Arguments:
<details>
<summary> Click to expand full list of arguments. </summary>

| Flag                             | Description                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| `-s`, `--sequences`              | Path to the main sequence file (.fasta)                                           |
| `-q`, `--query-id`               | ID of query sequence(s) within the alignment (mutually exclusive with `--reference-alignment`).                                |
| `-i`, `--include-queries-as-refs`               | If set, treat other --query-id sequences as references for each query (default: excluded).                                |
| `-r`, `--reference-sequences`    | Path to a separate reference alignment (must be the same nucleotide length; mutually exclusive with `--query-id`).   |
| `-n`, `--no-align`    | If set, skip MAFFT alignment before similarity plotting. Else, align sequences before plotting using `mafft --auto`.  |
| `-t`, `--threads`    | Number of threads to use for MAFFT alignment (default: 1).  |
| `-m`, `--metadata`               | Optional CSV/TSV file with sequence info (mapping accessions to genotypes). If provided, genotype information will be added to the output plots.   |
| `-mi`, `--metadata-id-col`       | Column name in metadata for sequence IDs (default: `Accession`).                           |
| `-mg`, `--metadata-genotype-col` | Column name in metadata for genotype info (default: `Genotype`).                           |
| `-mm`, `--metadata-mode`         | Whether metadata applies to `query`, `reference`, or `both` (default: `both`). |
| `-c`, `--colors`                 | Optional file mapping genotypes to colors (`tsv` or `csv`).                    |
| `-ws`, `--windowsize`             | Window size (default: 100).                                                    |
| `-ss`, `--stepsize`               | Step size between windows (default: 50).                                       |
| `-g`, `--gaps`                   | How to treat gaps: 0 = skip position if one or both sequences have a gap, 1 = mismatch if one has a gap, match if both have a gap, 2 = mismatch if one has a gap, skip position if both have a gap.  |
| `-f`, `--outformat`              | Output file format for the plots: `png`, `pdf`, `svg`, or `jpg` (default: `png`).                                      |
| `-ht`, `--height`               | Height of the entire figure in inches (default: 5.0).                             |
| `-wd`, `--width`               | Width of the plotting axes area in inches (default: 14.0).                             |
| `-p`, `--outplots`               | Directory for plot outputs (default: `simplots/`).                             |
| `-o`, `--outcsv`                 | Directory for CSV outputs (optional; if not provided, tables will not be saved).                                          |
| `-oa`, `--outaln`              | Output file path for alignment in fasta format (optional). If not provided, the alignment will not be saved.                                      |
</details>

### CSV / TSV templates
metadata.csv:
```
Accession, Genotype
Query1, Genotype A
Ref1, Genotype B
Ref2, Genotype C
```
Other column names for metadata can be specified using `--metadata-id-col` (`-mi`) and `--metadata-genotype-col` (`-mg`).

colors.csv
```
Genotype A,	#1f77b4
Genotype B,	#ff7f0e
Genotype C,	#2ca02c
```

### Example Usage
Simple run: 
```bash
python simplot.py \
    -s demo_data/query_alignment.fasta \
    -q OP137282.1 JX274981.1 \
    -ws 150 \
    -ss 50 \
    -p simplots \
    --no-align
```
With separate reference alignment:
```bash
python simplot.py \
    -s demo_data/query_alignment.fasta \
    -r demo_data/reference_alignment.fasta \
    -ws 200 \
    -ss 100 \
    -p simplots \
    --no-align
```
With metadata and custom colors:
```bash
python simplot.py \
    -s demo_data/query_alignment.fasta \
    -r demo_data/reference_alignment.fasta \
    -m demo_data/metadata.csv \
    -c demo_data/colors.tsv \
    --no-align
```
