# pyGenomeViz container

Main tool : [pyGenomeViz](https://moshi4.github.io/pyGenomeViz/)

Additional tools:
- ncbi-blast+ (2.12.0+ds-3+b1)
- mmseqs2 (14-7e284+ds-1+b2)
- mummer (3.23+dfsg-8)
- progressivemauve (1.2.0+4713+dfsg-5+b1)

Full documentation: https://moshi4.github.io/pyGenomeViz/

> pyGenomeViz is a genome visualization python package for comparative genomics implemented based on matplotlib. This package is developed for the purpose of easily and beautifully plotting genomic features and sequence similarity comparison links between multiple genomes.

## Example Usage

Using the CLI

```bash
# Download example dataset
pgv-download yersinia_phage

# Run BLAST CLI workflow
pgv-blast NC_070914.gbk NC_070915.gbk NC_070916.gbk NC_070918.gbk \
    -o pgv-blast_example --seqtype protein --show_scale_bar --curve \
    --feature_linewidth 0.3 --length_thr 100 --identity_thr 30

# Download example dataset
pgv-download mycoplasma_mycoides

# Run MUMmer CLI workflow
pgv-mummer GCF_000023685.1.gbff GCF_000800785.1.gbff GCF_000959055.1.gbff GCF_000959065.1.gbff \
    -o pgv-mummer_example --show_scale_bar --curve \
    --feature_type2color CDS:blue rRNA:lime tRNA:magenta

# Download example dataset
pgv-download enterobacteria_phage

# Run MMseqs CLI workflow
pgv-mmseqs NC_013600.gbk NC_016566.gbk NC_019724.gbk NC_024783.gbk NC_028901.gbk NC_031081.gbk \
    -o pgv-mmseqs_example --show_scale_bar --curve --feature_linewidth 0.3 \
    --feature_type2color CDS:skyblue --normal_link_color chocolate --inverted_link_color limegreen

# Download example dataset
pgv-download escherichia_coli

# Run progressiveMauve CLI workflow
pgv-pmauve NC_000913.gbk.gz NC_002695.gbk.gz NC_011751.gbk.gz NC_011750.gbk.gz \
    -o pgv-pmauve_example --show_scale_bar
```

This container contains the pygenomeviz python package, so custom scripts can import pygenomeviz

```python
from pygenomeviz import GenomeViz

gv = GenomeViz()
gv.set_scale_xticks(ymargin=0.5)

track = gv.add_feature_track("tutorial", 1000)
track.add_sublabel()

track.add_feature(50, 200, 1)
track.add_feature(250, 460, -1, fc="blue")
track.add_feature(500, 710, 1, fc="lime")
track.add_feature(750, 960, 1, fc="magenta", lw=1.0)

gv.savefig("features.png")
```
