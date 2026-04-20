# simplot-cl container

Main tool: [simplot-cl](https://github.com/hodcroftlab/simplot-cl)
  
Code repository: https://github.com/hodcroftlab/simplot-cl

Basic information on how to use this tool:
- executable: simplot.py
- help: `-h`
- description: A Command-Line Similarity Plot Generator

Additional tools:
- mafft: 7.505-1

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

Full documentation: https://github.com/hodcroftlab/simplot-cl/blob/main/README.md

## Example Usage
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
